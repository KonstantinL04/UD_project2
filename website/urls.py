from django.urls import path
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
]
