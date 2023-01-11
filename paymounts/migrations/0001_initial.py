# Generated by Django 4.0.7 on 2023-01-11 12:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paymount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=64, null=True)),
                ('status', models.CharField(max_length=64)),
                ('value', models.PositiveSmallIntegerField()),
                ('payment_method', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
