from django import forms
from django.core import validators
from hm_app.models import Comments

#Con ModelForm
class FormUser(forms.ModelForm):
    #Campos Personalizados

    class Meta:
        model = Comments
        #fields = "__all__"
        #fields = ('topic',)
        exclude = ('topic',)