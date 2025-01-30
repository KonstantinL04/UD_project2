# Generated by Django 4.2.17 on 2025-01-30 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('skills', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'positions',
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('production_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'production',
            },
        ),
        migrations.CreateModel(
            name='StagesProduction',
            fields=[
                ('stage_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'stages_production',
            },
        ),
        migrations.CreateModel(
            name='EmployeePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.employees')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.positions')),
            ],
            options={
                'db_table': 'employee_position',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('team', models.CharField(max_length=30)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.employees')),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.production')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.stagesproduction')),
            ],
            options={
                'db_table': 'schedule',
                'unique_together': {('schedule_id', 'production')},
            },
        ),
    ]
