from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class NewForm(forms.ModelForm):
    title = forms.CharField(max_length=128)

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            #категорию убираем из формы, чтобы пользователи сами не могли ее заполнять либо менять
            # категорию НЕ убираем из формы: менторы изменили задание. Теперь надо дать выбор при заполнении
            'categoryType',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")
        author = cleaned_data.get("author")
        categoryType = cleaned_data.get("categoryType")

        if title == text:
            raise ValidationError(
                "Заголовок не должен быть дентичен тексту."
            )
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data["title"]
        if title[0].islower():
            raise ValidationError(
                "Заглавие должно начинаться с заглавной буквы"
            )
        return title




