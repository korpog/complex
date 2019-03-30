from django.shortcuts import render, redirect
from .forms import ComplexForm

def index(request):
    if request.method == 'POST':
        form = ComplexForm(request.POST)
        if form.is_valid():
            real = form.cleaned_data['real']
            imag = form.cleaned_data['imag']
            root_degree = form.cleaned_data['root_degree']
            return redirect('results')
    else:
        form = ComplexForm()
    return render(request, 'index.html', {'form': form})
