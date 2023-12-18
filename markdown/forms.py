from django import forms

from .models import Markdown

class MarkdownForm(forms.ModelForm):
  class Meta:
    model = Markdown
    fields = [
        'nombre',
        'autor',
        'texto',
        ]
