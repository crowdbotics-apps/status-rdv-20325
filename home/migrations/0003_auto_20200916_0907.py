# Generated by Django 2.2.16 on 2020-09-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
