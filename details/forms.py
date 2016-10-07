from django import forms

class ContactMe(forms.Form):
	name = forms.CharField(
		required=True,
		max_length=40,
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'})
		)
	email_id = forms.CharField(
		required=True,
		max_length=40,
		widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'})
		)
	phone_no=forms.CharField(
		required=True,
		max_length=12,
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'})
		)
	message = forms.CharField(
		required=True,
		max_length=100,
		widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Message'})
		)