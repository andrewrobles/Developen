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

class CreateAccountForm(forms.Form):
	firstname = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'First name'
			}
		))
	lastname = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Last name'
			}
		))
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