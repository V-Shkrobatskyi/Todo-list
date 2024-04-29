from django import forms
from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    # deadline = forms.DateTimeField(required=False)
    # deadline = forms.DateTimeInput()
    # deadline = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
    #                                widget=forms.DateTimeInput(
    #                                    format='%d/%m/%Y %H:%M',
    #                                    attrs={'class': 'form-control', 'id': 'datetimepicker'}
    #                                )
    #                                )
    # deadline = forms.TextInput(attrs={'type': 'datetime-local'})
    # deadline = forms.DateTimeInput(attrs={'class': 'form-control', 'data - target': '  # datetimepicker1'})
    # deadline = forms.DateTimeField(input_formats=['%d/%m/%y %H:%M'])
    deadline = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
