from django.db import models

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'employees'

class Positions(models.Model):
    position_id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=255)
    skills = models.CharField(max_length=255)

    class Meta:
        db_table = 'positions'

class EmployeePosition(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)  
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)  
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'employee_position'

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

class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True) 
    production = models.ForeignKey(Production, models.DO_NOTHING)
    stage = models.ForeignKey('StagesProduction', models.DO_NOTHING)
    employee = models.ForeignKey(Employees, models.DO_NOTHING)
    team = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        db_table = 'schedule'
        unique_together = (('schedule_id', 'production'),)