from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
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
            'full_name': 'ФИО',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия Имя Отчество',
                'style': 'max-width: 300px;',
            }),
        }
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = mark_safe('<label for="id_full_name" class="form-label" style="font-weight: bold;">ФИО</label>')

class PositionForm(forms.ModelForm):
    class Meta:
        model = Positions
        fields = ['title', 'skills']
        labels = {
            'title': 'Название',
            'skills': 'Навыки',
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

    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = mark_safe('<label for="id_title" class="form-label" style="font-weight: bold;">Название</label>')
        self.fields['skills'].label = mark_safe('<label for="id_skills" class="form-label" style="font-weight: bold;">Навыки</label>')


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ['title', 'description']
        labels = {
            'title': 'Название',
            'description': 'Описание',
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
    def __init__(self, *args, **kwargs):
        super(ProductionForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = mark_safe('<label for="id_title" class="form-label" style="font-weight: bold;">Название</label>')
        self.fields['description'].label = mark_safe('<label for="id_description" class="form-label" style="font-weight: bold;">Описание</label>')


class StagesProductionForm(forms.ModelForm):
    class Meta:
        model = StagesProduction
        fields = ['title']
        labels = {
            'title': 'Стадия',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стадия',
                'style': 'max-width: 300px;',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(StagesProductionForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = mark_safe('<label for="id_title" class="form-label" style="font-weight: bold;">Название</label>')


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
    def __init__(self, *args, **kwargs):
        super(EmployeePositionForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].label = mark_safe('<label for="start_date" class="form-label" style="font-weight: bold;">Дата начала</label>')
        self.fields['end_date'].label = mark_safe('<label for="end_date" class="form-label" style="font-weight: bold;">Дата окончания</label>')

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

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['production'].label = mark_safe('<label for="id_production" class="form-label" style="font-weight: bold;">Постановка</label>')
        self.fields['stage'].label = mark_safe('<label for="id_stage" class="form-label" style="font-weight: bold;">Стадия</label>')
        self.fields['employee'].label = mark_safe('<label for="id_employee" class="form-label" style="font-weight: bold;">Сотрудник</label>')
        self.fields['team'].label = mark_safe('<label for="team" class="form-label" style="font-weight: bold;">Состав</label>')
        self.fields['start_time'].label = mark_safe('<label for="id_start_time" class="form-label" style="font-weight: bold;">Начало постановки</label>')
        self.fields['end_time'].label = mark_safe('<label for="id_end_time" class="form-label" style="font-weight: bold;">Конец постановки</label>')

