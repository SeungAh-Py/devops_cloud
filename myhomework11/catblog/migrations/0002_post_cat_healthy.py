# Generated by Django 3.2.9 on 2021-11-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cat_healthy',
            field=models.BooleanField(default=1, verbose_name='건강 양호'),
            preserve_default=False,
        ),
    ]
