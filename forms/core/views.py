from django.shortcuts import render

# Create your views here.

def formulario(requests):
	return render(requests, 'layout.html')