from django import forms
from .models import Blog, Comment, Hashtag


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['writer', 'title', 'body','hashtags','image']

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].label = ''
        self.fields['writer'].widget.attrs['placeholder'] = "Your email address"
        self.fields['title'].widget.attrs['placeholder'] = "Your subject of this message"
        self.fields['body'].widget.attrs['placeholder'] = "Say something about your today"
        self.fields['hashtags'].widget.attrs['placeholder'] = "#choice something"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']

