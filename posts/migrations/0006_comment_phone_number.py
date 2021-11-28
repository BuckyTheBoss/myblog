# Generated by Django 3.2.9 on 2021-11-28 12:11

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20211128_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+1234456788', max_length=128, region=None),
            preserve_default=False,
        ),
    ]
