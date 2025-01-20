from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Production
from .models import Employees, Positions, Production, StagesProduction, EmployeePosition, Schedule

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
    employees = Employees.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def positions_view(request):
    positions = Positions.objects.all()
    return render(request, 'positions.html', {'positions': positions})

def production_view(request):
    production = Production.objects.all()
    return render(request, 'production.html', {'production': production})

def stages_production_view(request):
    stages_production = StagesProduction.objects.all()
    return render(request, 'stages_production.html', {'stages_production': stages_production})

def employee_position_view(request):
    employee_position = EmployeePosition.objects.all()
    return render(request, 'employee_position.html', {'employee_position': employee_position})

def schedule_view(request):
    schedule = Schedule.objects.all()
    return render(request, 'schedule.html', {'schedule': schedule})