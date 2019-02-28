from django import forms

class SignInForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Username'
			}
		))
	password = forms.CharField(label='Password', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Password',
				'type':'password'
			}
		))