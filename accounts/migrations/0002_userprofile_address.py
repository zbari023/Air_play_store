# Generated by Django 4.2.4 on 2023-08-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
