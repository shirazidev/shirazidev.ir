# Generated by Django 4.2.6 on 2023-12-10 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
