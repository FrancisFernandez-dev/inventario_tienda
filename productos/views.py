from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Etiqueta, DetalleProducto

# -----------------------------
# INDEX
# -----------------------------
def index(request):
    return render(request, 'index.html')

# -----------------------------
# CRUD PRODUCTOS
# -----------------------------
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})


def crear_producto(request):
    categorias = Categoria.objects.all()
    etiquetas = Etiqueta.objects.all()

    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        precio = request.POST["precio"]
        categoria_id = request.POST["categoria"]

        categoria = Categoria.objects.get(id=categoria_id)

        # Crear producto base
        producto = Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            categoria=categoria
        )

        # Guardar etiquetas (ManyToMany)
        etiquetas_ids = request.POST.getlist("etiquetas")
        if etiquetas_ids:
            producto.etiquetas.set(etiquetas_ids)

        # Guardar detalles (OneToOne)
        dimension = request.POST.get("dimension")
        peso = request.POST.get("peso")

        if dimension or peso:
            DetalleProducto.objects.create(
                producto=producto,
                dimension=dimension,
                peso=peso
            )

        return redirect("lista_productos")

    return render(request, "productos/crear_producto.html", {
        "categorias": categorias,
        "etiquetas": etiquetas
    })


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.categoria_id = request.POST['categoria']
        producto.save()
        return redirect('lista_productos')

    return render(request, 'productos/editar_producto.html', {
        'producto': producto,
        'categorias': categorias
    })


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')


# -----------------------------
# DETALLE PRODUCTO
# -----------------------------
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    # Obtener OneToOne si existe
    try:
        detalles = producto.detalleproducto
    except DetalleProducto.DoesNotExist:
        detalles = None

    return render(request, 'productos/detalle_producto.html', {
        'producto': producto,
        'detalles': detalles
    })


# -----------------------------
# CRUD CATEGORÍAS
# -----------------------------
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'productos/listar_categorias.html', {'categorias': categorias})


def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        Categoria.objects.create(nombre=nombre)
        return redirect('listar_categorias')

    return render(request, 'productos/crear_categoria.html')


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        categoria.nombre = request.POST['nombre']
        categoria.save()
        return redirect('listar_categorias')

    return render(request, 'productos/editar_categoria.html', {
        'categoria': categoria
    })


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')

    return render(request, 'productos/eliminar_categoria.html', {
        'categoria': categoria
    })


# -----------------------------
# CRUD ETIQUETAS
# -----------------------------
def listar_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'productos/listar_etiquetas.html', {
        'etiquetas': etiquetas
    })


def crear_etiqueta(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        Etiqueta.objects.create(nombre=nombre)
        return redirect('lista_etiquetas')

    return render(request, 'productos/crear_etiqueta.html')


def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)

    if request.method == 'POST':
        etiqueta.nombre = request.POST['nombre']
        etiqueta.save()
        return redirect('lista_etiquetas')

    return render(request, 'productos/editar_etiqueta.html', {
        'etiqueta': etiqueta
    })


def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)

    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')

    return render(request, 'productos/eliminar_etiqueta.html', {
        'etiqueta': etiqueta
    })
