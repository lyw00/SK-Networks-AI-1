# Generated by Django 5.0.6 on 2024-06-12 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productImage',
            field=models.CharField(max_length=100, null=True),
        ),
    ]