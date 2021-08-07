from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Laptop

# Create your forms here.

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
		fields = ['status', 'cbhs_code', 'received_from', 'make', 'model', 
		'serial_number', 'worksheet_printed', 'cpu_model', 'cpu_speed', 'ram_in_gigabytes', 'storage', 'drive_capacity', 
		'does_it_boot', 'os_installed', 'battery_tested', 'hdd_ssd_chkdsk', 'cpu_temps', 'keyboard', 'trackpad', 
		'usb', 'display_out', 'actions_required', 'notes',
		'signed_off_by', 'sent_to']
