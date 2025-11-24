🛒 Proyecto Django – Gestión de Productos, Categorías y Etiquetas

Este proyecto es una aplicación web en Django que permite gestionar productos, categorías y etiquetas mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).
Incluye además una relación Uno a Uno para detalles adicionales de productos.

📌 Funcionalidades Principales
✅ Productos

Crear, listar, editar y eliminar productos.

Asignar cada producto a una categoría.

Añadir múltiples etiquetas (relación muchos a muchos).

Guardar detalles adicionales: dimensión y peso (relación uno a uno).

Ver detalles individuales de cada producto.

✅ Categorías

Crear, listar, editar y eliminar categorías.

Cada categoría puede estar asociada a múltiples productos.

✅ Etiquetas

Crear, listar, editar y eliminar etiquetas.

Cada etiqueta puede pertenecer a múltiples productos.

🌐 Página de inicio

Incluye un index simple para navegar entre las secciones.

🧱 Tecnologías utilizadas

Python 3.10

Django 5.2.6

SQLite como base de datos (por defecto)

HTML + CSS (incluye compatibilidad con dark mode)

📂 Estructura principal del proyecto
C:.
│   .gitignore
│   db.sqlite3
│   manage.py
│
├───productos
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   urls.py
│   │   views.py
│   ├───templates
│   │   └───productos (CRUD completo)
│   └───migrations
│
└───tienda
    │   settings.py
    │   urls.py
    │   wsgi.py

▶️ Cómo ejecutar el proyecto en local
1️⃣ Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate

2️⃣ Instalar dependencias
pip install django

3️⃣ Aplicar migraciones
python manage.py migrate

4️⃣ Ejecutar servidor
python manage.py runserver


Luego abre en tu navegador:

👉 http://127.0.0.1:8000/

📘 Modelos implementados
Producto

nombre

descripción

precio

categoría (ForeignKey)

etiquetas (ManyToMany)

detalleproducto (OneToOne)

Categoría

nombre

Etiqueta

nombre

DetalleProducto

dimension

peso

producto (OneToOne)

🧩 Próximas mejoras (opcional)

Autenticación de usuarios.

Paginación de productos.

Subida de imágenes para productos.

Panel de administración personalizado.

👤 Autor

Francis Fernandez
Proyecto desarrollado para evaluación de módulo Django – Talento Digital.
