# Generated by Django 3.2.12 on 2022-06-15 08:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='local_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]