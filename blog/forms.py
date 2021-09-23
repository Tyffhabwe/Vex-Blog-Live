from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Laptop

non_allowed_usernames = ['I can put any swear words here']
# Creating my own form tends to allow greater flexibility on what I can make it do.
class RegisterForm(forms.Form):
    # Registers users.
    username = forms.CharField(
    	label='Username',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "user-username"
            }
        )
    )
    email = forms.EmailField(
    	label='Email',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "user-email"
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-confirm-password"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if username in non_allowed_usernames:
            raise forms.ValidationError("This is an invalid username, please pick another.")
        if qs.exists():
            raise forms.ValidationError("This is an invalid username, please pick another.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email


    def clean_password(self):
    	password1 = self.cleaned_data.get("password1")
    	password2 = self.cleaned_data.get("password2")

    	if password1 != password2:
    		raise forms.ValidationError("Your two passwords seem not to match.")
    	elif password1 == password2:
    		return the_password
    	else:
    		raise forms.ValidationError("I have no idea what went wrong.")


class CreateLaptopForm(forms.ModelForm):
# Self explanatory. Form to create a laptop
	class Meta:
		model = Laptop
		# What can be edited
		fields = ['status', 'cbhs_code', 'received_from', 'model', 
		'os_installed', 'battery_tested',  'does_it_boot',
		'hdd_ssd_chkdsk', 
		'cpu_temps', 'keyboard', 'trackpad', 
		'usb', 'display_out', 'notes', 'sent_to']

		widgets = {
		# Styling the form so that it looks good
			'status': forms.Select(attrs={'class':'form-control'}),
			'cbhs_code': forms.TextInput(attrs={'class':'form-control'}),
			'received_from': forms.Select(attrs={'class':'form-control'}),
			'model': forms.Select(attrs={'class':'form-control'}),
			'os_installed': forms.Select(attrs={'class':'form-control'}),
			'battery_tested': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'hdd_ssd_chkdsk': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'does_it_boot': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'keyboard': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'trackpad': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'usb': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'display_out': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'notes': forms.Textarea(attrs={'class':'form-control'}),
			'sent_to': forms.Select(attrs={'class':'form-control'}),
		}
