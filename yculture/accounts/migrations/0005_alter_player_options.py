# Generated by Django 5.0.4 on 2024-04-29 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_merge_20240429_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name_plural': 'Player'},
        ),
    ]