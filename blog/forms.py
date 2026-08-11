from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            "titulo",
            "autor",
            "email",
            "conteudo",
        ]

        widgets = {
            "titulo": forms.TextInput(attrs={
                "placeholder": "Título do artigo"
            }),

            "autor": forms.TextInput(attrs={
                "placeholder": "Nome do autor"
            }),

            "email": forms.EmailInput(attrs={
                "placeholder": "E-mail"
            }),

            "conteudo": forms.Textarea(attrs={
                "placeholder": "Escreva seu artigo...",
                "rows": 12
            }),
        }