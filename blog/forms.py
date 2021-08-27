from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Laptop

# Create your forms here.

#Form to allow a new user to be created
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class CreateLaptopForm(forms.ModelForm):

	class Meta:
		model = Laptop
		#What can be edited
		fields = ['status', 'cbhs_code', 'received_from', 'model', 
		'does_it_boot', 'os_installed', 'battery_tested', 
		'hdd_ssd_chkdsk', 
		'cpu_temps', 'keyboard', 'trackpad', 
		'usb', 'display_out', 'notes',
		'technician', 'sent_to']

		widgets = {
		#Styling the form so that it looks good
			'status': forms.Select(attrs={'class':'form-control'}),
			'cbhs_code': forms.TextInput(attrs={'class':'form-control'}),
			'received_from': forms.Select(attrs={'class':'form-control'}),
			'model': forms.Select(attrs={'class':'form-control'}),
			'does_it_boot': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'os_installed': forms.Select(attrs={'class':'form-control'}),
			'battery_tested': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'hdd_ssd_chkdsk': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'does_it_boot': forms.NumberInput(attrs={'class':'form-control'}),
			'keyboard': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'trackpad': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'usb': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'display_out': forms.NullBooleanSelect(attrs={'class':'form-control'}),
			'notes': forms.Textarea(attrs={'class':'form-control'}),
			'technician': forms.Select(attrs={'class':'form-control'}),
			'sent_to': forms.Select(attrs={'class':'form-control'}),


		}
