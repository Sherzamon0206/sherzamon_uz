# Generated by Django 4.0.3 on 2022-03-09 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_about_description2'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='github',
            field=models.TextField(null=True),
        ),
    ]
