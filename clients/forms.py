# clients/forms.py
from django import forms
from .models import Client, Task

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        reason_for_roadblock = cleaned_data.get('reason_for_roadblock')
        
        if status == 'On Hold' and not reason_for_roadblock:
            raise forms.ValidationError(
                "When the status is 'On Hold', a reason for the roadblock must be selected."
            )
        
        return cleaned_data
    
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['action', 'assigned_to', 'due_date', 'status', 'comment']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'action': forms.Textarea(attrs={'rows': 3}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }