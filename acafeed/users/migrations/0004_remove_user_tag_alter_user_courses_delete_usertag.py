# Generated by Django 4.0.2 on 2022-03-23 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('users', '0003_user_blocked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tag',
        ),
        migrations.AlterField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(null=True, to='courses.Course'),
        ),
        migrations.DeleteModel(
            name='UserTag',
        ),
    ]
