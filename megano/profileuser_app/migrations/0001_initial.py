# Generated by Django 4.2.1 on 2023-06-09 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profileuser_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(default='Неизвестно', max_length=64, verbose_name='Ф.И.О.')),
                ('email', models.EmailField(default='Неизвестно', max_length=64, verbose_name='Email-адрес')),
                ('phone', models.CharField(default='Неизвестно', max_length=32, verbose_name='Номер телефона')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='AvatarUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='', upload_to=profileuser_app.models.avatar_path, verbose_name='Аватар')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to='profileuser_app.profileuser', verbose_name='Профиль пользователя')),
            ],
            options={
                'verbose_name': 'Аватар пользователя',
                'verbose_name_plural': 'Аватары пользователей',
                'ordering': ('pk',),
            },
        ),
    ]
