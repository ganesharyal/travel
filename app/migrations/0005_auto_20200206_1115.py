# Generated by Django 3.0 on 2020-02-06 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200206_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='PackageImage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
