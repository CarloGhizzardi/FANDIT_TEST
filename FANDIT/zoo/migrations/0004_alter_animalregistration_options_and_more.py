# Generated by Django 4.1.6 on 2023-03-05 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0003_alter_animalregistration_zoo_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animalregistration',
            options={'ordering': ['zoo_id']},
        ),
        migrations.RemoveField(
            model_name='animalregistration',
            name='family_id',
        ),
    ]