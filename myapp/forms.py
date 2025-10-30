from myapp.models import taskmanager
from django import forms
class taskForm(forms.ModelForm):
	class Meta:
		model=taskmanager
		fields='__all__'