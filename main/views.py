from django.shortcuts import render, redirect
from .forms import ComplexForm
from .utils import get_complex_roots, get_plot_components

def index(request):
    if request.method == 'POST':
        form = ComplexForm(request.POST)
        if form.is_valid():
            real = form.cleaned_data['real']
            imag = form.cleaned_data['imag']
            root_degree = form.cleaned_data['root_degree']
            z = complex(real, imag)
            roots = get_complex_roots(z, root_degree)
            x_vals = [z.real for z in roots]
            y_vals = [z.imag for z in roots]
            script, div = get_plot_components(x_vals, y_vals)
            return render(request, 'results.html', 
            {'roots_': roots, 'script': script, 'div': div})
    else:
        form = ComplexForm()
    return render(request, 'index.html', {'form': form})
