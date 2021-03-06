# Generated by Django 3.1.1 on 2020-09-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Имя')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
                ('subject', models.CharField(default=None, max_length=40)),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='static/portfolio')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=10)),
            ],
        ),
    ]
