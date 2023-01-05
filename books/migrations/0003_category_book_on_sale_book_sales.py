# Generated by Django 4.0.7 on 2023-01-04 16:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_discount_book_picture_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='sales',
            field=models.IntegerField(default=0),
        ),
    ]