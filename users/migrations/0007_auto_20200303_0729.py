# Generated by Django 2.2.7 on 2020-03-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200302_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
