# Generated by Django 3.2.3 on 2021-06-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('tole', models.CharField(max_length=300)),
                ('contact_no', models.CharField(max_length=300)),
                ('fax_no', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
            ],
        ),
    ]