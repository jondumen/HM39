from django import forms
from django.core import validators

#Con ModelForm
class FormUser(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(50)])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    catchbots = forms.CharField(required=False,
                                widget=forms.HiddenInput)
    
    #Funcion para verificar que los datos en "Catchbots" estan bien
    def clean_catchbots(self):
        catcher = self.cleaned_data['catchbots']
        if (len(catcher)>0):
            raise forms.ValidationError("Vaya, vaya Un botcito se esta portando mal hoy")
        return catcher