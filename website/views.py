from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home (request):
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
        return render (request,'home.html')

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