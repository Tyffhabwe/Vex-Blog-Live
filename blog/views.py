import openpyxl
import logging
import os

from datetime import datetime
from openpyxl import load_workbook
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Post, Laptop
from django.contrib.auth.decorators import login_required
from .filters import LaptopFilter
from .forms import NewUserForm, CreateLaptopForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse


def true_or_false(pc_variable):
	"""Takes the datetime in excel sheet and turns it into a boolean"""
	if pc_variable == "y" or pc_variable == "Yes":
		pc_variable = True
	elif pc_variable == "n":
		pc_variable = False
	else:
		x = "This is just a placeholder!"
	return pc_variable

def change_date_to_needed(time_value):
	"""Takes the time format in excel sheet and converts it to what is needed by django"""
	try:
		dic = []
		dic = time_value.split('-') #splits up our variables
		#logging.critical(dic)
		dic_value_to_use = dic[2]
		second_dic = dic_value_to_use.split(' ')
		logging.critical(dic)
		logging.critical(second_dic)
		year =  dic[0]
		month = dic[1]
		date = second_dic[0]

		new_date_value = datetime(int(year), int(month), int(date))

		return(new_date_value)
	except:
		return(datetime.now())

# Create your views here.
def frontpage(request):
	posts = Post.objects.all()
	return render(request, 'blog/frontpage.html', {'posts': posts})

def post_detail(request, slug):
	post = Post.objects.get(slug=slug)

	return render(request, 'blog/post_detail.html', {'post': post})

def view_database(request):
	laptops = Laptop.objects.all()
	my_filter = LaptopFilter(request.GET, queryset=laptops)
	laptops = my_filter.qs
	return render(request, 'blog/view_database.html', {'laptops': laptops, 'my_filter': my_filter})

def laptop_detail(request, laptop_id):
	laptop = Laptop.objects.get(pk=laptop_id)

	return render(request, 'blog/laptop_detail.html', {'laptop': laptop})

"""def create_laptop_view(request):
	context = {}

	user = request.user

	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateLaptopForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		worked_on_by = User.objects.filter(email=user.email).first()
		obj.worked_on_by = worked_on_by
		obj.save()

		form = CreateLaptopForm()

	context['form'] = form

	return render(request, 'blog/create_laptop.html', context)
"""
def must_authenticate(request):
	return render(request, 'blog/must_authenticate.html')

@login_required
def create_laptop_view(request):
	form = CreateLaptopForm(request.POST or None, request.FILES or None)

	context = {

		'form':form
	}

	if form.is_valid():
		laptop = form.save()
		return HttpResponseRedirect('/')

	return render(request, 'blog/create_laptop.html', context)

def update_view(request, laptop_id):
	laptop = get_object_or_404(Laptop, id=laptop_id)
	form = CreateLaptopForm(request.POST or None, request.FILES or None, instance=laptop)

	if form.is_valid():
		laptop.save()
		return HttpResponseRedirect(reverse('view_database'))

	context = {

		'form':form,
		'laptop':laptop

	}
	return render(request, 'blog/create_laptop.html', context)




def get_data(request):

	workbook = load_workbook(filename="laptop_tracking.xlsx")

	sheet = workbook.active

	for row in sheet.iter_rows(min_row=3, values_only=True):
		#Adding the data
		status = row[1]
		cbhs_code =  row[2]
		date_received = str(row[3])
		received_from = row[4]
		make = row[5]
		model = row[6]
		serial_number = row[7]
		worksheet_printed = row[8]
		cpu_model = row[9]
		cpu_speed = row[10]
		ram_in_gigabytes = row[11]
		storage = row[12]
		drive_capacity = row[13]
		does_it_boot = row[14]
		os_installed =  row[15]
		battery_tested =  row[16]
		hdd_ssd_chkdsk = row[17]
		cpu_temps =  row[18]
		keyboard = row[20]
		trackpad = row[21]
		usb = row[22]	
		display_out = row[23]
		actions_required = row[24]
		date_last_worked_on = str(row[25])
		notes = row[26]
		worked_on_by = row[27]
		signed_off_by = row[28]
		sent_to = row[29]
		slug = row[30]

		_, created = Laptop.objects.get_or_create(
			status = status,
			cbhs_code =  cbhs_code,
			date_received = change_date_to_needed(date_received),
			received_from = received_from,
			make = make,
			model = model,
			serial_number = serial_number,
			worksheet_printed = true_or_false(worksheet_printed),
			cpu_model = cpu_model,
			cpu_speed = cpu_speed,
			ram_in_gigabytes = ram_in_gigabytes,
			storage = storage,
			drive_capacity = drive_capacity,
			does_it_boot = true_or_false(does_it_boot),
			os_installed =  os_installed,
			battery_tested =  battery_tested,
			hdd_ssd_chkdsk = true_or_false(hdd_ssd_chkdsk),
			cpu_temps =  cpu_temps,
			keyboard = true_or_false(keyboard),
			trackpad = true_or_false(trackpad),
			usb = true_or_false(usb),
			display_out = true_or_false(display_out),
			actions_required = actions_required,
			date_last_worked_on = change_date_to_needed(date_last_worked_on),
			notes = notes,
			worked_on_by = worked_on_by,
			signed_off_by = signed_off_by,
			sent_to = sent_to,
			slug = slug,
		 	)
	return HttpResponse("It worked!")
		 	
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("frontpage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="blog/register.html", context={"register_form":form})