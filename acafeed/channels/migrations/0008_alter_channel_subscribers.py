# Generated by Django 3.2.12 on 2022-03-29 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_courses'),
        ('channels', '0007_alter_reply_reply_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='subscribers',
            field=models.ManyToManyField(blank=True, to='users.User'),
        ),
    ]
