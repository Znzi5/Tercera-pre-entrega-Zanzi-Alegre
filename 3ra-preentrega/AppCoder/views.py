from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm
from .forms import TuFormulario

def insertar_datos(request):
    if request.method == 'POST':
        tu_formulario = TuFormulario(request.POST)
        categoria_form = CategoriaForm(request.POST)
        producto_form = ProductoForm(request.POST)
        cliente_form = ClienteForm(request.POST)

        if categoria_form.is_valid() and producto_form.is_valid() and cliente_form.is_valid():
            categoria_form.save()
            producto_form.save()
            cliente_form.save()
            return redirect('insertar_datos')

    else:
        categoria_form = CategoriaForm()
        producto_form = ProductoForm()
        cliente_form = ClienteForm()

    return render(request, 'insertar_datos.html', {
        'categoria_form': categoria_form,
        'producto_form': producto_form,
        'cliente_form': cliente_form,
    })

def buscar_datos(request):
    if request.method == 'POST':
        tu_formulario = TuFormulario(request.POST)
        # Resto de la lógica...
        return render(request, 'resultados_busqueda.html', {'tu_formulario': tu_formulario})
    else:
        tu_formulario = TuFormulario()
        return render(request, 'buscar_datos.html', {'tu_formulario': tu_formulario})
