# Generated by Django 3.2.9 on 2021-12-12 21:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_shop_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='shop/Shop/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]