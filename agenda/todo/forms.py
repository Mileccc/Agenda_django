from django.forms import ModelForm, DateInput
from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ('date',)
        widgets = {
            'estimated_end': DateInput(attrs={'type': 'date'})
        }
