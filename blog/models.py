from django.db import models

# Create your models here.
class Post(models.Model):
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


class Laptop(models.Model):
	status = models.CharField(max_length=255, null=True)
	cbhs_code =  models.CharField(max_length=255, null=True)
	date_received = models.DateTimeField(null=True)
	received_from = models.CharField(max_length=255, null=True)
	make = models.CharField(max_length=255, null=True)
	model = models.CharField(max_length=255, null=True)
	serial_number = models.CharField(max_length=255, null=True)
	worksheet_printed = models.BooleanField(null=True)
	cpu_model = models.CharField(max_length=255, null=True)
	cpu_speed = models.CharField(max_length=255, null=True)
	ram_in_gigabytes = models.IntegerField(null=True)
	storage = models.CharField(max_length=255, null=True)
	drive_capacity = models.IntegerField(null=True)
	does_it_boot = models.BooleanField(null=True)
	os_installed =  models.CharField(max_length=255, null=True)
	battery_tested =  models.IntegerField(null=True)
	hdd_ssd_chkdsk = models.BooleanField(null=True)
	cpu_temps =  models.IntegerField(null=True)
	keyboard = models.BooleanField(null=True)
	trackpad = models.BooleanField(null=True)
	usb = models.BooleanField(null=True)
	display_out = models.BooleanField(null=True)
	actions_required = models.TextField(null=True)
	date_last_worked_on = models.DateTimeField(null=True)
	notes = models.TextField(null=True)
	worked_on_by = models.CharField(max_length=255, null=True)
	signed_off_by = models.CharField(max_length=255, null=True)
	sent_to = models.CharField(max_length=255, null=True)
	slug = models.SlugField(null=True)

	class Meta:
		ordering = ['-cbhs_code']

	def __str__(self):
		return str(self.cbhs_code)
	



