# Generated by Django 5.0.6 on 2025-05-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Household', '0002_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=20),
        ),
    ]
