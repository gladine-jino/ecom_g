# Generated by Django 3.2.12 on 2022-12-01 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_customer_itemssaled_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='flowers-4929984.jpg', null=True, upload_to=''),
        ),
    ]