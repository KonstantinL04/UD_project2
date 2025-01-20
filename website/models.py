from django.db import models

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'employees'  # Укажите имя существующей таблицы


class Positions(models.Model):
    position_id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=255)
    skills = models.CharField(max_length=255)

    class Meta:
        db_table = 'positions'


class Production(models.Model):
    production_id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'production'


class StagesProduction(models.Model):
    stage_id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=255)

    class Meta:
        db_table = 'stages_production'


class EmployeePosition(models.Model):
    position = models.OneToOneField('Positions', models.DO_NOTHING, primary_key=True)  # The composite primary key (position_id, employee_id) found, that is not supported. The first column is selected.
    employee = models.ForeignKey('Employees', models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'employee_position'
        unique_together = (('position', 'employee'),)


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)  # The composite primary key (schedule_id, production_id) found, that is not supported. The first column is selected.
    production = models.ForeignKey(Production, models.DO_NOTHING)
    stage = models.ForeignKey('StagesProduction', models.DO_NOTHING)
    employee = models.ForeignKey(Employees, models.DO_NOTHING)
    team = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        db_table = 'schedule'
        unique_together = (('schedule_id', 'production'),)