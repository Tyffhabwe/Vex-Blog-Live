
from django.contrib import admin
from django.urls import path, include

from blog.views import *


urlpatterns = [
    # different urls and what functions they call to so that an html file can be called.
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('view_database', view_database, name='view_database'),
    path("register", register_request, name="register"),
    path("laptop/<int:laptop_id>/", laptop_detail, name='laptop_detail'),
    path('laptop/new', create_laptop_view, name='create_laptop_view'),
    path('laptop/update/<int:laptop_id>', update_view, name='update')
]
