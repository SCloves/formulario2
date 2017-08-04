from django.shortcuts import render

# Create your views here.

def formulario(requests):
	return render(requests, 'core.templates.layout.html')