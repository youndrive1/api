from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    body = forms.CharField(label='댓글', widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['body']