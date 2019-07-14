# Generated by Django 2.2.2 on 2019-07-02 16:33

from django.db import migrations, models
import ej_users.utils


class Migration(migrations.Migration):

    dependencies = [("ej_users", "0001_ada_lovelace_v1")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="display_name",
            field=models.CharField(
                default=ej_users.utils.random_name,
                help_text="Name used to publicly identify user",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="passwordresettoken",
            name="url",
            field=models.CharField(
                default=ej_users.utils.token_factory, max_length=50, unique=True, verbose_name="User token"
            ),
        ),
    ]
