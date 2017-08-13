from django import forms

class PatientForm(forms.Form):
    bool = forms.BooleanField(label='Boolean', required=False)
    patientid = forms.CharField(label='Patient ID', max_length=100)
