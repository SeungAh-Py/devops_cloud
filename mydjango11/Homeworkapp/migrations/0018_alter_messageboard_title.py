# Generated by Django 3.2.9 on 2021-11-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homeworkapp', '0017_alter_messageboard_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageboard',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]