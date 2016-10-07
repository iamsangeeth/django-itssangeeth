from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'})
    )
    email_id = forms.EmailField(
        max_length=40,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email', 'class': 'form-control'})
    )
    comment_text = forms.CharField(
        max_length=300,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Comment', 'class': 'form-control'})
    )

