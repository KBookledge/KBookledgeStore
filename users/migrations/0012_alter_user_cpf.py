# Generated by Django 4.1.5 on 2023-01-10 18:25

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_alter_user_cpf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="cpf",
            field=cpf_field.models.CPFField(
                max_length=11, unique=True, verbose_name="cpf"
            ),
        ),
    ]