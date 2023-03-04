# Generated by Django 4.1.6 on 2023-03-04 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
        ('animal', '0002_remove_animal_zoo_id'),
        ('zoo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal')),
                ('family_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family.family')),
                ('zoo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoo.zoo')),
            ],
            options={
                'ordering': ['family_id'],
            },
        ),
    ]