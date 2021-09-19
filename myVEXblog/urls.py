
from django.contrib import admin
from django.urls import path, include

from blog.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('view_database', view_database, name='view_database'),
    path("register", register_request, name="register"),
    path("laptop/<int:laptop_id>/", laptop_detail, name='laptop_detail'),
    path('must_authenticate', must_authenticate, name='must_authenticate'),
    path('laptop/new', create_laptop_view, name='create_laptop_view'),
    path('laptop/update/<int:laptop_id>', update_view, name='update')
]
