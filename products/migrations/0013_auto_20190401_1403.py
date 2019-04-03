# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-01 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20190401_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Extras',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='catergories.Extra'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Mens',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='catergories.Men'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Unisexs',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='catergories.Unisex'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Womens',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='catergories.Women'),
        ),
    ]
