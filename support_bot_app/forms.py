from django import forms


class ReplyMessageForm(forms.Form):
    text = forms.CharField(
        label='Text',
        widget=forms.Textarea(
            attrs={'placeholder': 'Your message'}
        )
    )
