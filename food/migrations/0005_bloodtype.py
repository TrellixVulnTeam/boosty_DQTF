# Generated by Django 3.1 on 2022-06-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20200914_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10)),
            ],
        ),
    ]
