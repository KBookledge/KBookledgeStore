# Generated by Django 4.0.7 on 2023-01-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_pdf_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='categorys',
            field=models.ManyToManyField(blank=True, related_name='books', to='books.category'),
        ),
    ]
