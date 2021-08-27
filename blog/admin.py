from django.contrib import admin

# Register your models here.
from .models import *

#This allows me to edit my tables in the admin table
admin.site.register(Post)
admin.site.register(Operating_System)
admin.site.register(Laptop_Model)
admin.site.register(Provider)
admin.site.register(Receiver)
admin.site.register(Laptop)


