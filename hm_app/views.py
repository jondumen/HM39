from django.shortcuts import render
from hm_app.models import Producer, Comments
from . import forms

# Create your views here.
def index(request):
	comm = Comments.objects.order_by('name')
	prod = Producer.objects.order_by('name')
	print(prod)
	my_context = {'username': 'Hana dice Hola desde Views.py',
			   #'producers': prod
	  }
	return render(request, 'hm_app/index.html', context=my_context)

#Crear un formulario para mostrar
def comment_form(request):
	form = forms.FormUser(request.POST)

	#print(request.method)
	if form.is_valid():
		print("Validado Exitosamente! :D")
		print("Name: ", form.cleaned_data['name'])
		print("Email: ", form.cleaned_data['email'])
		print("Text: ", form.cleaned_data['text'])
		print(form.cleaned_data['catchbots'])
		comment = Comments.objects.get_or_create(name=form.cleaned_data['name'], 
										   		email=form.cleaned_data['email'], 
												text=form.cleaned_data['text'])[0]
		comment.save()

	return render(request, 'hm_app/comment_form.html', {'form' : form})

def producers(request):
    prod = Producer.objects.order_by('name')
    return render(request, 'hm_app/producers.html', {'producers': prod})
