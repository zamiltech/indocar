# Generated by Django 3.2.12 on 2022-06-15 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(default='', max_length=200, unique=True, verbose_name='Company name')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Company',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('Offer_id', models.AutoField(primary_key=True, serialize=False)),
                ('Total_Price', models.PositiveSmallIntegerField(verbose_name='Total Price')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Created Date')),
                ('Company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.company')),
                ('Offer_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offer',
            },
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place_name', models.CharField(default='', max_length=200, unique=True, verbose_name='Place name')),
            ],
            options={
                'verbose_name': 'Places',
                'verbose_name_plural': 'Places',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_name', models.CharField(default='', max_length=100, unique=True, verbose_name='Service name')),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Price_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numbers_of_Pax', models.PositiveSmallIntegerField(default=1, verbose_name='Numbers of Pax')),
                ('Price', models.PositiveSmallIntegerField(verbose_name='Price')),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.places')),
                ('Service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.services')),
            ],
            options={
                'verbose_name': 'Price Plan',
                'verbose_name_plural': 'Price Plan',
            },
        ),
        migrations.CreateModel(
            name='Offer_line',
            fields=[
                ('Offer_line_id', models.AutoField(primary_key=True, serialize=False)),
                ('Numbers_of_Pax', models.PositiveSmallIntegerField(default=1, verbose_name='Numbers of Pax')),
                ('Price', models.PositiveSmallIntegerField(verbose_name='Price')),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.places')),
                ('Service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.services')),
                ('offer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.offer')),
            ],
            options={
                'verbose_name': 'Offer Lines',
                'verbose_name_plural': 'Offer Lines',
            },
        ),
    ]
