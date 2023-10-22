from django import forms
from .models import Employee,Search

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','age','email','username','position','designation','phone_number','image']
    def clean_username(self):
        username = self.cleaned_data['username']
        if Employee.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already in use. Please choose a different one.')
        return username

class SearchForm(forms.ModelForm):
    class Meta:
        model=Search
        fields="__all__"

    name = forms.CharField(required=False)
    designation = forms.CharField(required=False)
    position = forms.CharField(required=False)

class DeleteForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['name','email']

class EditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','age','email','position','designation','phone_number','image']