# Generated by Django 3.1.7 on 2021-09-18 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210911_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='sent_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.receiver'),
        ),
    ]
