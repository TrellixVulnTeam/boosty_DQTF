# Generated by Django 3.1 on 2022-06-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_bloodtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodtype',
            name='id',
        ),
        migrations.AlterField(
            model_name='bloodtype',
            name='name',
            field=models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10, primary_key=True, serialize=False),
        ),
    ]
