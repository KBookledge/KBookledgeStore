# Generated by Django 4.0.7 on 2023-01-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf_book',
            field=models.FileField(max_length=30, upload_to=''),
            preserve_default=False,
        ),
    ]
