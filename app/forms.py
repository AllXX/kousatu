from datetime import datetime
from django import forms
from .models import Thread,Comment

class SearchForm(forms.Form):
    keyword = forms.CharField(label='検索', max_length=200)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title','message')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'message')
