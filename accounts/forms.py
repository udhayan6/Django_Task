from django import forms 

# creating a form 
class InputForm(forms.Form): 

	user_name = forms.CharField(max_length = 200) 
	password = forms.CharField(widget = forms.PasswordInput()) 
