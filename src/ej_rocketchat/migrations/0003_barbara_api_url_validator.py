# Generated by Django 2.2.2 on 2019-07-13 21:50

from django.db import migrations, models
import ej_rocketchat.validators


class Migration(migrations.Migration):

    dependencies = [("ej_rocketchat", "0002_barbara_rc1")]

    operations = [
        migrations.AlterField(
            model_name="rcconfig",
            name="api_url",
            field=models.CharField(
                blank=True,
                help_text="A private URL used only for API calls. Can be used to override the public URL if Rocket.Chat is also available from an internal address in your network.",
                max_length=200,
                null=True,
                unique=True,
                validators=[ej_rocketchat.validators.WhiteListedURLValidator()],
                verbose_name="Rocket.Chat private URL",
            ),
        )
    ]