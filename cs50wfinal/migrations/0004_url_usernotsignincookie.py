# Generated by Django 4.0 on 2022-01-04 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs50wfinal', '0003_url_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='userNotSignInCookie',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
