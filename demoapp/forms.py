from django import forms


class NameForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
    }), label='Enter your First Name:', max_length=100)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
    }),label='Enter your Last Name:', max_length=100)
