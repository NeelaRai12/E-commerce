# Generated by Django 3.2.3 on 2021-06-10 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='name',
        ),
        migrations.AddField(
            model_name='blog',
            name='label',
            field=models.CharField(choices=[('new', 'New Product'), ('hot', 'Hot Product'), ('sale', 'Sale Product')], default='new', max_length=60),
        ),
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('In', 'In Stock'), ('Out', 'Out of Stock')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
