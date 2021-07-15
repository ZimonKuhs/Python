# Generated by Django 3.2.5 on 2021-07-15 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('register_date', models.DateTimeField(verbose_name='Date registered.')),
                ('weight', models.DecimalField(decimal_places=3, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Macros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('kCal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('carbs', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=8)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fiber', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sugar', models.DecimalField(decimal_places=2, max_digits=8)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.person')),
            ],
        ),
    ]
