# Generated by Django 2.1.3 on 2018-12-08 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("ej_users", "0003_add_is_used_field")]

    operations = [migrations.RemoveField(model_name="user", name="display_name")]
