from django.shortcuts import render, redirect
from .forms import ComplexForm
from .utils import get_complex_roots

def index(request):
    if request.method == 'POST':
        form = ComplexForm(request.POST)
        if form.is_valid():
            real = form.cleaned_data['real']
            imag = form.cleaned_data['imag']
            root_degree = form.cleaned_data['root_degree']
            z = complex(real, imag)
            roots = get_complex_roots(z, root_degree)
            return render(request, 'results.html', {'roots': roots})
    else:
        form = ComplexForm()
    return render(request, 'index.html', {'form': form})
