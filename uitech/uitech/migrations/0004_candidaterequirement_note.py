# Generated by Django 5.1 on 2024-08-31 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uitech', '0003_candidaterequirement_salary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidaterequirement',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
