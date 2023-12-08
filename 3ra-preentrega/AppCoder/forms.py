# myapp/forms.py

from django import forms
from .models import Categoria, Producto, Cliente



class TuFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    # Otros campos y lógica del formulario si es necesario


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']
