# Generated by Django 3.2.8 on 2021-10-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_submission_last_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='assigned',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submission',
            name='last_submission',
            field=models.DateTimeField(auto_now=True, default='2020-01-01'),
            preserve_default=False,
        ),
    ]
