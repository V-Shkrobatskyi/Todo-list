from django import forms
from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        input_formats=['%d:%m:%Y %H:%M'],
        widget=forms.DateTimeInput(
            format='%d:%m:%Y %H:%M',
        ),
        required=False,
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
