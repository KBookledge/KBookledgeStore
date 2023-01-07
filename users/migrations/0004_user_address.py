# Generated by Django 4.0.7 on 2023-01-05 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adresses', '0001_initial'),
        ('users', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='adresses.address'),
            preserve_default=False,
        ),
    ]
