from django.shortcuts import render
from .forms import PostForm

# Create your views here.

def formulario(requests):
	form = PostForm()
	return render(requests, 'core/layout.html', {'form': form})