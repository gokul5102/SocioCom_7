# Generated by Django 3.2.7 on 2021-09-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='gst_no',
            field=models.CharField(default='123456789012345', max_length=15),
        ),
    ]