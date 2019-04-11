# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-10 20:20
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catergories', '0006_auto_20190409_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='option',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('XXXSmall', 'XXXSmall'), ('XXSmall', 'XXSmall'), ('XSmall', 'XSmall'), ('Small', 'Small'), ('MMedium', 'Medium'), ('Large', 'Large'), ('XLarge', 'XLarge'), ('XXLarge', 'XXLarge'), ('XXXLarge', 'XXXLarge'), ('6', '6'), ('6.5', '6.5'), ('7', '7'), ('7.5', '7.5'), ('8', '8'), ('8.5', '8.5'), ('9', '9'), ('10', '10'), ('10.5', '10.5'), ('11', '11'), ('12', '12')], default=0, max_length=101, null=True),
        ),
    ]
