import django_filters

from .models import Laptop

#Search bar filter and what it will show.
class LaptopFilter(django_filters.FilterSet):
	class Meta:
		model = Laptop
		fields = '__all__'
		exclude = ['date_received', 'sent_to', 'slug', 'received_from', 'make', 'serial_number', 'worksheet_printed',
		'cpu_speed', 'ram_in_gigabytes', 'storage', 'drive_capacity', 'does_it_boot', 'os_installed', 'cpu_model', 
		'battery_tested', 'hdd_ssd_chkdsk', 'cpu_temps', 'keyboard', 'trackpad', 'usb', 'display_out', 'windows_activated',
		'actions_required', 'date_last_worked_on', 'signed_off_by', 'password_expires', 'technician', 'notes', 'model'
		]