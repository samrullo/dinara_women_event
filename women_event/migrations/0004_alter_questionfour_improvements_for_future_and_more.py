# Generated by Django 4.2 on 2025-02-16 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_event', '0003_responder_education_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionfour',
            name='improvements_for_future',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questionthree',
            name='seminar_topic_other',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='questiontwo',
            name='difficulties_in_japan_other',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='questiontwo',
            name='your_priority_problem',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='responder',
            name='workplace',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
