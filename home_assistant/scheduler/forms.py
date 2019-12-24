from django import forms
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'executor', 'author', 'description', 'active', 'done', 'start_date',
                  'end_date', 'start_time', 'everyday', 'day_of_month']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Записать задачу'))


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'executor', 'author', 'description', 'active', 'done', 'start_date',
                  'end_date', 'start_time', 'everyday', 'day_of_month']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Сохранить изменения'))
