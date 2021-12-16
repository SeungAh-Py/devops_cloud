# Generated by Django 3.2.10 on 2021-12-16 21:33

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shop',
            name='telephone',
            field=models.CharField(help_text='입력 예시) 042-1234-5678', max_length=15, validators=[django.core.validators.RegexValidator('^\\d{3,4}-?\\d{3,4}-?\\d{4}$')]),
        ),
    ]
