from django import forms

from .models import Post, Comment,student

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class studentForm(forms.ModelForm):

    class Meta:
        model = student
        fields = ('name','std_id','mobile','email','department')
