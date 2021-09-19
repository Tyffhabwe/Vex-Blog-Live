# Generated by Django 3.1.7 on 2021-09-18 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0015_auto_20210918_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='technician',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]