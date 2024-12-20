from django import forms
from .models import News, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']