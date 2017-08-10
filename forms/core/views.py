from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib import messages
from forms.core.models import Formulario

# Create your views here.

def formulario(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.nome = request.POST['nome']
            post.email = request.POST['email']
            post.telefone = request.POST['telefone']
            post.save()
            messages.success(
            request, "Seus dados foram registrados. Em breve entraremos em contato.")
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'core/layout.html', {'form': form})


def lista_inscritos(request):
    inscritos = Formulario.objects.all()
    template_name = 'core/inscritos.html'
    context = {'inscritos': inscritos}
    return render(request, template_name, context)


def info_inscrito(request, pk):
    inscrito = get_object_or_404(Formulario, pk=pk)
    template_name = 'core/info_inscrito.html'
    context = {'inscrito': inscrito}
    return render(request, template_name, context)