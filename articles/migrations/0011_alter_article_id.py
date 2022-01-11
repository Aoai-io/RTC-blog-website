# Generated by Django 4.0.1 on 2022-01-11 07:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_article_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
