# Generated by Django 3.2.9 on 2021-11-29 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homeworkapp', '0006_auto_20211129_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageboard',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='작성시간'),
        ),
    ]
