from django import forms
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Column, Row, MultiField, Field
from crispy_forms.bootstrap import FormActions
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'executor', 'notify',
                  'scheduled', 'start_date', 'end_date', 'start_time', 'monday',
                  'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
                  'sunday']
        widgets = {
            'due_date': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': True,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
            'start_date': DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': True,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
                ), 
            'end_date': DatePicker(
                options={
                    'useCurrent': True,
                    'collapse': True,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
            'start_time': TimePicker(
                options={
                    'useCurrent': True,
                    'collapse': True,
                },
                attrs={
                    'append': 'fa fa-clock-o',
                    'icon_toggle': True,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Новая задача',
                'name',
                'description',
                'due_date',
                'executor',
                'notify',
                'scheduled'
            ),
            Fieldset(
                'Расписание',
                Row(
                    Column('start_date'),
                    Column('end_date')
                ),
                'start_time',
                Fieldset(
                    'Дни недели',
                    Row(
                        Column('monday'),
                        Column('tuesday'),
                        Column('wednesday'),
                        Column('thursday'),
                        Column('friday'),
                        Column('saturday'),
                        Column('sunday'),
                    )
                )
            ),
            FormActions(
                Submit('submit', 'Записать')
            )
        )


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'executor', 'notify',
                  'scheduled', 'start_date', 'end_date', 'start_time', 'monday',
                  'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
                  'sunday']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Сохранить изменения'))
