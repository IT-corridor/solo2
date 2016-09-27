# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-27 01:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import seller.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to=b'')),
                ('thumb', models.ImageField(upload_to=b'')),
                ('business_name', models.CharField(max_length=100)),
                ('business_owner_name', models.CharField(max_length=100)),
                ('business_address', models.CharField(max_length=100)),
                ('business_phone', models.IntegerField()),
                ('business_cell_phone', models.CharField(max_length=20)),
                ('business_email', models.EmailField(max_length=254)),
                ('business_owner_email', models.EmailField(max_length=254)),
                ('business_description', models.TextField()),
                ('business_contact_name', models.CharField(max_length=100)),
                ('permit_type', models.CharField(max_length=50)),
                ('permit_expiration_date', models.DateTimeField()),
                ('permit_number', models.IntegerField()),
                ('delivery_method', models.CharField(max_length=100)),
                ('delivery_service_provider', models.CharField(max_length=100)),
                ('began_at', models.DateTimeField()),
                ('time_zone', models.CharField(blank=True, max_length=50, null=True)),
                ('url_pinterest', models.CharField(max_length=100)),
                ('url_instagram', models.CharField(max_length=100)),
                ('url_facebook', models.CharField(max_length=100)),
                ('url_twitter', models.CharField(max_length=100)),
                ('url_yelp', models.CharField(max_length=100)),
                ('url_business_website', models.CharField(max_length=100)),
                ('yelp_rating', models.FloatField()),
                ('yelp_comments', models.TextField()),
                ('customer_rating', models.FloatField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BakerComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('text', models.TextField()),
                ('baker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Baker')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=seller.models.generate_id, max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'')),
                ('type', models.CharField(max_length=30)),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6)),
                ('min_order_amount', models.DecimalField(decimal_places=2, default=1.0, max_digits=6)),
                ('min_order_unit', models.IntegerField(default=1)),
                ('photo', models.FileField(upload_to=b'')),
                ('delivery_method', models.CharField(max_length=100)),
                ('delivery_service', models.CharField(max_length=100)),
                ('delivery_fee', models.FloatField()),
                ('hashtags', models.CharField(max_length=50)),
                ('ingredients', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('num_views', models.IntegerField()),
                ('num_likes', models.IntegerField()),
                ('num_shares', models.IntegerField()),
                ('num_orders', models.IntegerField()),
                ('customer_rating', models.FloatField()),
                ('fulfilment_time', models.CharField(max_length=100)),
                ('caption', models.CharField(blank=True, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('baker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Baker')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('text', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('session', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('traffic_source', models.CharField(max_length=100)),
                ('first_visit_date', models.DateTimeField()),
                ('visits_prior_checkout', models.IntegerField()),
                ('avarage_time_on_pages', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('delivery_address', models.CharField(max_length=100)),
                ('likes', models.TextField()),
                ('shares', models.TextField()),
                ('comments', models.TextField()),
                ('baker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Baker')),
            ],
        ),
    ]