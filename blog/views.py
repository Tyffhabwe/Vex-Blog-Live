#My dependacies, often just files from other pages
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
from .forms import RegisterForm, CreateLaptopForm
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

#Function for what pages the frontpage displayes
def frontpage(request):
	posts = Post.objects.all()
	return render(request, 'blog/frontpage.html', {'posts': posts})

#Function to take data from database and display it onto a table
def view_database(request):
	laptops = Laptop.objects.all()
	my_filter = LaptopFilter(request.GET, queryset=laptops)
	laptops = my_filter.qs
	return render(request, 'blog/view_database.html', {'laptops': laptops, 'my_filter': my_filter})
#Displays individual laptopdata from the view_database page.
def laptop_detail(request, laptop_id):
	laptop = Laptop.objects.get(pk=laptop_id)

	return render(request, 'blog/laptop_detail.html', {'laptop': laptop})

#Redirect users that have not authenticated
def must_authenticate(request):
	return render(request, 'blog/must_authenticate.html')

@login_required #Make sure users have authenticated
def create_laptop_view(request):
	form = CreateLaptopForm(request.POST or None, request.FILES or None)

	context = {

		'form':form
	}

	if form.is_valid():
		laptop = form.save(commit=False)
		laptop.technician = request.user
		laptop.save()
		return HttpResponseRedirect('/')

	return render(request, 'blog/create_laptop.html', context)

#For page that allows new laptops to be made/edit existing ones
@login_required
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
	return render(request, 'blog/edit_laptop.html', context)

# Allows the user to register a new account
def register_request(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password1")
		password2 = form.cleaned_data.get("password2")
		if len(password2) >= 8:
			if password == password2:
				try:
					user = User.objects.create_user(username, email, password2)
				except:
					user = None
				if user != None:
					login(request, user)
					return redirect("/")
			else:
				messages.error(request, "Your two passwords do not match")
		else:
			request.session['register_error'] = 1
			messages.error(request, "Your password needs to be at least 8 characters long.")
	return render(request, "blog/register.html", {"form":form})       		
	
