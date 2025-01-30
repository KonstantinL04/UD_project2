from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Employees, Positions, Production, Schedule, StagesProduction, EmployeePosition

class SignUpForm(UserCreationForm): 
    email = forms.EmailField(label ="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Электронная почта" }
        ),
    )

    first_name = forms.CharField(label="", max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Фамилия" }
        ),
    )
    last_name = forms.CharField(label="", max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Имя"}
        ),
    )

    class Meta:
        model = User
        fields = ( 
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def __init__(self, *args,**kwargs):
        super (SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Имя пользователя"
        self.fields["username"].label = ""
        self.fields[
            "username"
        ].help_text = '<span class="form-text text-muted"><small>*Обятельно. Не более 150 символов. Только буквы, цифры и @/./+/-/_.</small></span>'

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Пароль"
        self.fields["password1"].label = ""
        self.fields[
            "password1"
        ].help_text = "<ul class=\"form-text text-muted small\"><li>*Придумайте пароль, не содержащий личную информацию.</li><li>*Пароль должен быть не менее 8 символов.</li></ul>"

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Подтвердите пароль"
        self.fields["password2"].label = ""
        self.fields[
            "password2"
        ].help_text = '<span class="form-text text-muted"><small>*Повторно введите придуманный пароль.</small></span>'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['full_name']
        labels = {
            'full_name': '',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия Имя Отчество',
                'style': 'max-width: 300px;',
            }),
        }

class PositionForm(forms.ModelForm):
    class Meta:
        model = Positions
        fields = ['title', 'skills']
        labels = {
            'title': '',
            'skills': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
                'style': 'max-width: 300px;',
            }),

            'skills': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Навыки',
                'style': 'max-width: 300px;',
            }),
        }

class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ['title', 'description']
        labels = {
            'title': '',
            'description': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
                'style': 'max-width: 300px;',
            }),

            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
                'style': 'max-width: 300px;',
            }),
        }

class StagesProductionForm(forms.ModelForm):
    class Meta:
        model = StagesProduction
        fields = ['title']
        labels = {
            'title': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стадия',
                'style': 'max-width: 300px;',
            }),
        }

class EmployeePositionForm(forms.ModelForm):
    class Meta:
        model = EmployeePosition
        fields = ['start_date', 'end_date','position','employee']
        labels = {
            'start_date': 'Дата начала',
            'end_date': 'Дата окончания',
            'position': '',
            'employee': '',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'type': 'date',
            }),

            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'type': 'date',

            }),

            'position': forms.HiddenInput(attrs={
                'id': 'position_id'
            }),

            'employee': forms.HiddenInput(attrs={
                'id': 'employee_id'
            }),
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['production', 'stage', 'employee', 'team', 'start_time', 'end_time']
        labels = {
            'production': '',
            'stage': '',
            'employee': '',
            'team': 'Состав',
            'start_time': 'Начало постановки',
            'end_time': 'Конец постановки',
        }
        widgets = {
            'production': forms.HiddenInput(attrs={
                'id': 'production_id'
                }),
            'stage': forms.HiddenInput(attrs={
                'id': 'stage_id'
                }),
            'employee': forms.HiddenInput(attrs={
                'id': 'employee_id'
                }),
            
            'team': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите состав',
                'style': 'max-width: 300px;',
            }),

            'start_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Начало',
                'style': 'max-width: 300px;',
                'type': 'datetime-local'
            }),

            'end_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Окончание',
                'style': 'max-width: 300px;',
                'type': 'datetime-local'
            }),
        }

