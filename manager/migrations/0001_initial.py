# Generated by Django 4.2.5 on 2023-09-26 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='additem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(default=0, max_length=50)),
                ('Description', models.CharField(default=0, max_length=100)),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='addmanager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(default=0, max_length=50)),
                ('LastName', models.CharField(default=0, max_length=50)),
                ('EmailAddress', models.CharField(default=0, max_length=50)),
                ('PhoneNumber', models.IntegerField(default=0)),
                ('Address', models.TextField(default=0)),
                ('PostalCode', models.IntegerField(default=0)),
            ],
        ),
    ]
