# Generated by Django 4.0.1 on 2022-01-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='instructors/'),
        ),
    ]
