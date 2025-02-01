# Generated by Django 4.2.17 on 2025-02-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudiencesSchedule',
            fields=[
                ('audiences_schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time_production', models.DateTimeField()),
                ('end_time_production', models.DateTimeField()),
            ],
            options={
                'db_table': 'audiences_schedule',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='employeeposition',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
