# Generated by Django 5.1.7 on 2025-03-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_list',
            name='assigned_by',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='todo_list',
            name='priority',
            field=models.CharField(choices=[('High', 'high'), ('Low', 'low'), ('Medium', 'medium')], max_length=6),
        ),
        migrations.AlterField(
            model_name='todo_list',
            name='status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Completed', 'completed')], max_length=9),
        ),
        migrations.AlterField(
            model_name='todo_list',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
