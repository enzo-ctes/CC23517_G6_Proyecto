# Generated by Django 5.0 on 2023-12-12 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_about_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['created'], 'verbose_name': 'integrante', 'verbose_name_plural': 'integrantes'},
        ),
    ]
