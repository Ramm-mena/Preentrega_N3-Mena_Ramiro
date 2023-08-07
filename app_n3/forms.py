from django import forms 

class vintaje_club(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.IntegerField(label="apellido", required=True)
    email = forms.EmailField(label="Email", required=False)