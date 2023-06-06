from django.forms import ModelForm
from .models import DailyTask


class DailyTasksForm(ModelForm):
    class Meta:
        model = DailyTask
        fields = ['title', 'memo', 'important']