# Generated by Django 4.0.7 on 2023-01-05 18:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('neighborhood', models.CharField(max_length=64)),
                ('street_address', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=9)),
                ('complement', models.TextField(blank=True, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
