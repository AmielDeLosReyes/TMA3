# Generated by Django 4.1.7 on 2023-04-01 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TMA3', '0002_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_firstname', models.CharField(max_length=140)),
                ('customer_lastname', models.CharField(max_length=140)),
                ('customer_email', models.CharField(max_length=140)),
                ('customer_pass', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=140)),
                ('product_image', models.CharField(max_length=140)),
                ('product_price', models.CharField(max_length=140)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMA3.customer')),
            ],
        ),
        migrations.DeleteModel(
            name='Part2',
        ),
    ]
