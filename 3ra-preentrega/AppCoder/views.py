from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm
from .forms import TuFormulario

def insertar_datos(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        producto_form = ProductoForm(request.POST)
        cliente_form = ClienteForm(request.POST)

        if categoria_form.is_valid() and producto_form.is_valid() and cliente_form.is_valid():
            categoria = categoria_form.save()
            producto = producto_form.save(commit=False)
            producto.categoria = categoria  # Asociar producto con la categoría
            producto.save()
            
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
        if tu_formulario.is_valid():
            # Obtén los datos del formulario
            criterio_busqueda = tu_formulario.cleaned_data.get('criterio_busqueda')
            
            # Realiza la búsqueda en la base de datos
            resultados_categoria = Categoria.objects.filter(nombre__icontains=criterio_busqueda)
            resultados_producto = Producto.objects.filter(nombre__icontains=criterio_busqueda)
            resultados_cliente = Cliente.objects.filter(nombre__icontains=criterio_busqueda)

            return render(request, 'resultados_busqueda.html', {
                'tu_formulario': tu_formulario,
                'resultados_categoria': resultados_categoria,
                'resultados_producto': resultados_producto,
                'resultados_cliente': resultados_cliente,
            })
    
    else:
        tu_formulario = TuFormulario()

    return render(request, 'buscar_datos.html', {'tu_formulario': tu_formulario})
