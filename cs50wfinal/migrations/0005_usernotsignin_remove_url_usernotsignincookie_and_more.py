# Generated by Django 4.0 on 2022-01-04 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cs50wfinal', '0004_url_usernotsignincookie'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotSignIn',
            fields=[
                ('cookie', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='url',
            name='userNotSignInCookie',
        ),
        migrations.AddField(
            model_name='url',
            name='userNotSignIn',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cs50wfinal.usernotsignin'),
        ),
    ]