from django import forms

def username_validate(value):
	user_error = ['new', 'butt', 'sexy', 'dick', 'django', 'facebook', 'twiter']
	if value in user_error:
		raise forms.ValidationError('Enter valid Username')
	if len(value) <= 3:
		raise forms.ValidationError('Enter valid Username')

	else:
		return value

	return value



	

