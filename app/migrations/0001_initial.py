# Generated by Django 3.2.6 on 2021-08-31 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_firstname', models.CharField(max_length=100)),
                ('emp_lastname', models.CharField(max_length=100)),
                ('emp_address', models.CharField(max_length=100)),
                ('emp_city', models.CharField(max_length=100)),
            ],
        ),
    ]