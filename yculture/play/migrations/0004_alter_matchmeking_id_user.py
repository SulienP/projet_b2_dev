# Generated by Django 5.0.4 on 2024-04-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0003_matchmeking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchmeking',
            name='id_user',
            field=models.IntegerField(null=True),
        ),
    ]