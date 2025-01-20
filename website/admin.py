from django.contrib import admin
from .models import Employees, Positions, Production, StagesProduction, EmployeePosition, Schedule

admin.site.register(Employees)
admin.site.register(Positions)
admin.site.register(Production)
admin.site.register(StagesProduction)
admin.site.register(EmployeePosition)
admin.site.register(Schedule)


