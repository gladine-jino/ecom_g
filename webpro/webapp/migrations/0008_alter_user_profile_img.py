# Generated by Django 4.0.4 on 2022-12-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='media_root/product_images/reg.jpg', upload_to=''),
        ),
    ]