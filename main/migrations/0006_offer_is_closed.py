# Generated by Django 3.2.12 on 2022-06-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220616_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='is_closed',
            field=models.BooleanField(default=False, verbose_name='Is Closed?'),
        ),
    ]
