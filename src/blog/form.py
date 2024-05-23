from django import forms
from .models import Comment
# Create your form here.



class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ['comment']
    