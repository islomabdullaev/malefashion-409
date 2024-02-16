from django import forms

from blogs.models import CommentModel

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ("name", "phone", "email", "text")
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'text': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
        }
