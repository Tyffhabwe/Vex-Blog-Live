from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#All of the options for status a laptop/desktop will have
status_choice = [
	('In Progress', 'In Progress'),
	('Waiting for Parts', 'Waiting for Parts'),
	('Complete', 'Complete'),
]
class Post(models.Model):
	"""This is a 'table' for posts and what values each post will have"""
	title = models.CharField(max_length=255)
	slug = models.SlugField()
	intro = models.TextField()
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date_added']

	def __str__(self):
		"""Convenient for Admin Table"""
		return self.title

class Operating_System(models.Model):
	"""One of the many to one tables to allow me to create values for what OS is running on a device"""
	name = models.CharField(max_length=255, null=True)

	def __str__(self):
		"""Convenient for Admin Table as it displays an actual OS rather than just text"""
		return self.name

class Laptop_Model(models.Model):
	"""One of the many to one tables to allow me to create values for the different models of laptop"""
	model_name = models.CharField(max_length=255, null=True)
	resolution = models.CharField(max_length=255, null=True)
	processor = models.CharField(max_length=255, null=True)
	processor_speed = models.CharField(max_length=255, null=True)
	connectivity = models.CharField(max_length=255, null=True)
	RAM = models.CharField(max_length=255, null=True)
	storage = models.IntegerField(null=True)
	notes = models.TextField(max_length=255, null=True)

	def __str__(self):
		"""Convenient for Admin Table as it displays an actual OS rather than just text"""
		return self.model_name

	class Meta:
		"""Helps decide what order to display the model if I choose to do that. It will use model_name"""
		ordering = ['-model_name']

class Provider(models.Model):
	"""One of the many to one tables to allow me to create values for the different organisations we get laptops from"""
	provider_name = models.CharField(max_length=255, null=True)
	email = models.CharField(max_length=255, null=True)
	telephone = models.CharField(max_length=255, null=True)
	notes = models.TextField(max_length=255, null=True)

	def __str__(self):
		"""Convenient for Admin Table as it displays an actual OS rather than just text"""
		return self.provider_name

class Receiver(models.Model):
	"""One of the many to one tables to allow me to create values for the different organisations we give laptops to"""
	receiver_name = models.CharField(max_length=255, null=True)
	email = models.CharField(max_length=255, null=True)
	telephone = models.CharField(max_length=255, null=True)
	notes = models.TextField(max_length=255, null=True)

	def __str__(self):
		"""Convenient for Admin Table as it displays an actual OS rather than just text"""
		return self.receiver_name

class Laptop(models.Model):
	"""This is the 'table' for laptops and what values each laptop will have. Some are many-to-one relationships with another table."""
	status = models.CharField(choices=status_choice, null=True, max_length=255)
	cbhs_code =  models.CharField(max_length=255, null=True)
	date_received = models.DateTimeField(null=True)
	received_from = models.ForeignKey(Provider, null=True, blank=True, on_delete=models.CASCADE)
	model = models.ForeignKey(Laptop_Model, null=True, blank=True, on_delete=models.CASCADE)
	does_it_boot = models.BooleanField(null=True)
	os_installed =  models.ForeignKey(Operating_System, null=True, blank=True, on_delete=models.CASCADE)
	battery_tested =  models.BooleanField(null=True)
	hdd_ssd_chkdsk = models.BooleanField(null=True)
	cpu_temps =  models.IntegerField(null=True, blank=True)
	keyboard = models.BooleanField(null=True)
	password_expires = models.BooleanField(null=True)
	windows_activated = models.BooleanField(null=True)
	trackpad = models.BooleanField(null=True)
	usb = models.BooleanField(null=True)
	display_out = models.BooleanField(null=True)
	date_last_worked_on = models.DateTimeField(null=True)
	notes = models.TextField(null=True, blank=True)
	signed_off_by = models.CharField(max_length=255, null=True, blank=True)
	sent_to = models.ForeignKey(Receiver, null=True, blank=True, on_delete=models.CASCADE)
	technician = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	class Meta:
		ordering = ['-cbhs_code']

	def __str__(self):
		return str(self.cbhs_code)
	



