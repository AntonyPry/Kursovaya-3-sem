# Generated by Django 4.2.7 on 2023-11-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_alter_rental_end_date_alter_rental_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalrental',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='active', max_length=20),
        ),
        migrations.AddField(
            model_name='rental',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='active', max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='price_per_day',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
