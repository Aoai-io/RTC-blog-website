# Generated by Django 4.0 on 2021-12-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='posted_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]