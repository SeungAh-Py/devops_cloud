# Generated by Django 3.2.9 on 2021-11-29 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bbs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
                ('date', models.DateTimeField(verbose_name='작성시간')),
                ('mobile', models.CharField(max_length=11, verbose_name='연락처')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('context', models.TextField(verbose_name='내용')),
            ],
        ),
    ]
