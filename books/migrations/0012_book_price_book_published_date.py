# Generated by Django 5.2.3 on 2025-07-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
