from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget = forms.Textarea())

    class Meta:
        model = Article
        fields = (
            'title',
            'content'
        )