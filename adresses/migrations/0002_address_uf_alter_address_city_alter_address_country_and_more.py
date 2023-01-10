# Generated by Django 4.0.7 on 2023-01-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adresses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='uf',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='Brasil', max_length=64),
        ),
        migrations.AlterField(
            model_name='address',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(default='S/N', max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_address',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]