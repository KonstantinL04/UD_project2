from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Production
from .models import Employees, Positions, Production, StagesProduction, EmployeePosition, Schedule
from django.core.paginator import Paginator
from .forms import EmployeeForm, PositionForm, ProductionForm, StagesProductionForm, EmployeePositionForm, ScheduleForm
from django.urls import reverse

def home (request):
    productions = Production.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success (request, "Вы вошли в систему.")
            return redirect('home')
        else:
            messages.warning(request,"Произошла ошибка, попробуйте еще раз")
            return redirect('home')
    else:
        return render (request,'home.html', {'productions': productions})

def logout_user(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли.')
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success (request, "Вы зарегистрировались.")
            return redirect('home')
        else:
            messages.error(request, "Произошла ошибка при регистрации.")
    return render(request, "register.html", {'form': form})

def employees_view(request):
    employees_list = Employees.objects.all()
    paginator = Paginator(employees_list, 30)  # Показывать 30 сотрудников на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'employees.html', {'page_obj': page_obj})

def positions_view(request):
    positions = Positions.objects.all()
    paginator = Paginator(positions, 30)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'positions.html', {'page_obj': page_obj})

def production_view(request):
    production = Production.objects.all()
    paginator = Paginator(production, 30)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'production.html', {'page_obj': page_obj})

def stages_production_view(request):
    stages_production = StagesProduction.objects.all()
    paginator = Paginator(stages_production, 30)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'stages_production.html', {'page_obj': page_obj})

def employee_position_view(request):
    employee_position = EmployeePosition.objects.select_related('employee', 'position').order_by('start_date').all()
    paginator = Paginator(employee_position, 30)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'employee_position.html', {'page_obj': page_obj})

def schedule_view(request):
    schedule = Schedule.objects.select_related('production', 'stage', 'employee').order_by('schedule_id').all()
    paginator = Paginator(schedule, 30)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'schedule.html', {'page_obj': page_obj})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сотрудник успешно добавлен.')
            return redirect('employees')
    else:
        form = EmployeeForm()
    return render(request, 'add_record.html', {'form': form, 'return_url': reverse('employees')})

def add_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Должность успешно добавлена.')
            return redirect('positions')
    else:
        form = PositionForm()
    return render(request, 'add_record.html', {'form': form, 'return_url': reverse('positions')})

def add_production(request):
    if request.method == 'POST':
        form = ProductionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Постановка успешно добавлена.')
            return redirect('production')
    else:
        form = ProductionForm()
    return render(request, 'add_record.html', {'form': form, 'return_url': reverse('production')})

def add_stages_production(request):
    if request.method == 'POST':
        form = StagesProductionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Стадия постановки успешно добавлена.')
            return redirect('stages_production')
    else:
        form = StagesProductionForm()
    return render(request, 'add_record.html', {'form': form, 'return_url': reverse('stages_production')})

def add_employee_position(request):
    if request.method == 'POST':
        form = EmployeePositionForm(request.POST)
        if form.is_valid():
            position = form.cleaned_data['position']
            employee = form.cleaned_data['employee']
            print(f"Position: {position}, Employee: {employee}")  # Отладочное сообщение
            if EmployeePosition.objects.filter(position=position, employee=employee).exists():
                messages.error(request, 'Должность сотрудника с этой должностью уже существует.')
                print("Duplicate entry found")  # Отладочное сообщение
            else:
                form.save()
                messages.success(request, 'Должность сотрудника успешно добавлена.')
                print("Form saved successfully")  # Отладочное сообщение
                return redirect('employee_position')
        else:
            print("Form errors:", form.errors)  # Отладочное сообщение
    else:
        form = EmployeePositionForm()
    employees = Employees.objects.all()
    positions = Positions.objects.all()
    return render(request, 'add_employee_position.html', {'form': form, 'positions': positions, 'employees': employees, 'return_url': reverse('employee_position')})

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Расписание успешно добавлено.')
            return redirect('schedule')
    else:
        form = ScheduleForm()
    productions = Production.objects.all()
    stages = StagesProduction.objects.all()
    employees = Employees.objects.all()
    return render(request, 'add_schedule.html', {'form': form, 'productions': productions, 'stages': stages, 'employees': employees, 'return_url': reverse('schedule')})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employees, employee_id=employee_id)
    employee.delete()
    messages.success(request, 'Сотрудник успешно удален.')
    return redirect('employees')

def delete_position(request, position_id):
    position = get_object_or_404(Positions, position_id=position_id)
    position.delete()
    messages.success(request, 'Должность успешно удалена.')
    return redirect('positions')

def delete_production(request, production_id):
    production = get_object_or_404(Production, production_id=production_id)
    production.delete()
    messages.success(request, 'Постановка успешно удалена.')
    return redirect('production')

def delete_stages_production(request, stage_id):
    stage = get_object_or_404(StagesProduction, stage_id=stage_id)
    stage.delete()
    messages.success(request, 'Стадия постановки успешно удалена.')
    return redirect('stages_production')

def delete_employee_position(request, id):
    employee_position = get_object_or_404(EmployeePosition, id=id)
    employee_position.delete()
    messages.success(request, 'Должность сотрудника успешно удалена.')
    return redirect('employee_position')

def delete_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, schedule_id=schedule_id)
    schedule.delete()
    messages.success(request, 'Расписание успешно удалено.')
    return redirect('schedule')

def employee_detail(request, employee_id):
    employee = Employees.objects.get(employee_id=employee_id)
    return render(request, 'employee_detail.html', {'employee': employee})

def position_detail(request, position_id):
    position = Positions.objects.get(position_id=position_id)
    return render(request, 'position_detail.html', {'position': position})

def production_detail(request, production_id):
    production = Production.objects.get(production_id=production_id)
    return render(request, 'production_detail.html', {'production': production})

def stages_production_detail(request, stage_id):
    stage = StagesProduction.objects.get(stage_id=stage_id)
    return render(request, 'stages_production_detail.html', {'stage': stage})

def employee_position_detail(request, id):
    employee_position = get_object_or_404(EmployeePosition, id=id)
    return render(request, 'employee_position_detail.html', {'employee_position': employee_position})

def schedule_detail(request, schedule_id):
    schedule = Schedule.objects.get(schedule_id=schedule_id)
    return render(request, 'schedule_detail.html', {'schedule': schedule})

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employees, employee_id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сотрудник успешно обновлен.')
            return redirect('employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})

def edit_position(request, position_id):
    position = get_object_or_404(Positions, position_id=position_id)
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            messages.success(request, 'Должность успешно обновлена.')
            return redirect('positions')
    else:
        form = PositionForm(instance=position)
    return render(request, 'edit_position.html', {'form': form})

def edit_production(request, production_id):
    production = get_object_or_404(Production, production_id=production_id)
    if request.method == 'POST':
        form = ProductionForm(request.POST, instance=production)
        if form.is_valid():
            form.save()
            messages.success(request, 'Постановка успешно обновлено.')
            return redirect('production')
    else:
        form = ProductionForm(instance=production)
    return render(request, 'edit_production.html', {'form': form})

def edit_stages_production(request, stage_id):
    stage = get_object_or_404(StagesProduction, stage_id=stage_id)
    if request.method == 'POST':
        form = StagesProductionForm(request.POST, instance=stage)
        if form.is_valid():
            form.save()
            messages.success(request, 'Стадия постановки успешно обновлена.')
            return redirect('stages_production')
    else:
        form = StagesProductionForm(instance=stage)
    return render(request, 'edit_stage_production.html', {'form': form})

def edit_employee_position(request, id):
    employee_position = get_object_or_404(EmployeePosition, id=id)
    positions = Positions.objects.all()
    employees = Employees.objects.all()
    if request.method == 'POST':
        form = EmployeePositionForm(request.POST, instance=employee_position)
        if form.is_valid():
            position_name = request.POST.get('position_name')
            employee_name = request.POST.get('employee_name')
            if position_name and employee_name:
                position = Positions.objects.get(title=position_name)
                employee = Employees.objects.get(full_name=employee_name)
                employee_position.position = position
                employee_position.employee = employee
            form.save()
            messages.success(request, 'Должность сотрудника успешно обновлена.')
            return redirect('employee_position')
    else:
        form = EmployeePositionForm(instance=employee_position)
    return render(request, 'edit_employee_position.html', {'form': form, 'employee_position': employee_position, 'positions': positions, 'employees': employees})

def edit_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, schedule_id=schedule_id)
    productions = Production.objects.all()
    stages = StagesProduction.objects.all()
    employees = Employees.objects.all()
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            production_name = request.POST.get('production_name')
            stage_name = request.POST.get('stage_name')
            employee_name = request.POST.get('employee_name')
            if production_name and stage_name and employee_name:
                production = Production.objects.get(title=production_name)
                stage = StagesProduction.objects.get(title=stage_name)
                employee = Employees.objects.get(full_name=employee_name)
                schedule.production = production
                schedule.stage = stage
                schedule.employee = employee
            form.save()
            messages.success(request, 'Расписание успешно обновлено.')
            return redirect('schedule')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'edit_schedule.html', {'form': form, 'schedule': schedule, 'productions': productions, 'stages': stages, 'employees': employees})

