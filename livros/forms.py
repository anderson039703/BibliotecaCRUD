from django import forms

from livros.models import Livros


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        filter = '__all__'
