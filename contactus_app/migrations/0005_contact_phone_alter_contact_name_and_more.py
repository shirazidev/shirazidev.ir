# Generated by Django 4.2.6 on 2023-10-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0004_alter_contact_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Phone',
            field=models.CharField(default=980000000000, max_length=17),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=30),
        ),
    ]