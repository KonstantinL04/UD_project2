from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('employees/', views.employees_view, name='employees'),
    path('positions/', views.positions_view, name='positions'),
    path('production/', views.production_view, name='production'),
    path('stages_production/', views.stages_production_view, name='stages_production'),
    path('employee_position/', views.employee_position_view, name='employee_position'),
    path('schedule/', views.schedule_view, name='schedule'),

    path('add_employee/', views.add_employee, name='add_employee'),
    path('add_position/', views.add_position, name='add_position'),
    path('add_production/', views.add_production, name='add_production'),
    path('add_stages_production/', views.add_stages_production, name='add_stages_production'),
    path('add_employee_position/', views.add_employee_position, name='add_employee_position'),
    path('add_schedule/', views.add_schedule, name='add_schedule'),

    path('__debug__/', include('debug_toolbar.urls')),

    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('positions/<int:position_id>/', views.position_detail, name='position_detail'),
    path('production/<int:production_id>/', views.production_detail, name='production_detail'),
    path('stages_production/<int:stage_id>/', views.stages_production_detail, name='stages_production_detail'),
    path('employee_position/<int:id>/', views.employee_position_detail, name='employee_position_detail'),
    path('schedule/<int:schedule_id>/', views.schedule_detail, name='schedule_detail'),

    path('employees/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('employee_position/delete/<int:id>/', views.delete_employee_position, name='delete_employee_position'),
    path('positions/delete/<int:position_id>/', views.delete_position, name='delete_position'),
    path('production/delete/<int:production_id>/', views.delete_production, name='delete_production'),
    path('stages_production/delete/<int:stage_id>/', views.delete_stages_production, name='delete_stages_production'),
    path('schedule/delete/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),

    path('employees/edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('positions/edit/<int:position_id>/', views.edit_position, name='edit_position'),
    path('production/edit/<int:production_id>/', views.edit_production, name='edit_production'),
    path('stages_production/edit/<int:stage_id>/', views.edit_stages_production, name='edit_stages_production'),
    path('employee_position/edit/<int:id>/', views.edit_employee_position, name='edit_employee_position'),
    path('schedule/edit/<int:schedule_id>/', views.edit_schedule, name='edit_schedule'),


]
