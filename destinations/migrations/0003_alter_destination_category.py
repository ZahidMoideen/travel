# Generated by Django 5.0.6 on 2024-05-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_alter_destination_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='category',
            field=models.CharField(choices=[('Beach', 'Beach'), ('Mountain', 'Mountain'), ('City', 'City'), ('Historical', 'Historical')], max_length=20),
        ),
    ]
