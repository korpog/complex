from django import forms

class ComplexForm(forms.Form):
    real = forms.FloatField(label="Real")
    imag = forms.FloatField(label="Imaginary")
    root_degree = forms.IntegerField(min_value=1, label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['real'].widget.attrs.update({'class': 'form-control'})
        self.fields['imag'].widget.attrs.update({'class': 'form-control'})
        self.fields['root_degree'].widget.attrs.update({'class': 'form-control'})