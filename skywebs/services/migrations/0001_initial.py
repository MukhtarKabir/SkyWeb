# Generated by Django 5.1.5 on 2025-02-24 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_name', models.CharField(help_text="Enter the icon class name (e.g., 'fa fa-code')", max_length=50)),
                ('title', models.CharField(help_text='Enter the service title', max_length=100)),
                ('description', models.TextField(help_text='Enter a brief description of the service')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
