# Generated by Django 5.0 on 2023-12-12 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indumentaria', '0002_alter_indumentaria_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='indumentaria',
            name='historico',
            field=models.BooleanField(default=False),
        ),
    ]
