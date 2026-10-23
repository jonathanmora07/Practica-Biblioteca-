# Instrucciones para el proyecto 
## Aplicacion web con python - Flask - Bootstrap. 
### Biblioteca escolar. 

# Dependecias 
1. Utilizar Requirements.txt
2. utilizar la bliblioteca de flask 

# Objetivo de la practica.
En esta practica se utilizaran los conocimientos adquiridos previamente en la practica anterior,
para aprender el como dar los primeros pasos en la creacion de paginas web y el uso de los comandos bootstrap. 
Tambien se reforzo el uso de GitHub como nube para ver los avances del proyecto. 

# Práctica: Sitio Web de Biblioteca Universitaria con Flask y Bootstrap

Este proyecto consiste en una aplicación web multipágina desarrollada con Python y Flask para una biblioteca escolar/universitaria, aplicando renderizado de plantillas Jinja2, herencia de vistas y componentes de Bootstrap.

### 1. Servidor Principal (`server.py`)
- **Punto de entrada:** Configura la aplicación de Flask y gestiona las peticiones HTTP del usuario.
- **Rutas creadas:** Se definieron 4 rutas principales (`/`, `/catalogo`, `/servicios` y `/contacto`).
- **Paso de variables:** Cada ruta utiliza la función `render_template()` para enviar dinámicamente las variables `titulo` y `mensaje` a sus respectivas plantillas HTML.

### 2. Plantilla Base y Herencia (`templates/layout.html`)
- **Estructura HTML principal:** Contiene los elementos compartidos por todo el sitio (`<head>`, hojas de estilo CSS y librerías JavaScript de Bootstrap).
- **Menú de navegación:** Incorpora una barra de navegación horizontal (`navbar`) con un estilo de Bootstrap en tono azul (`bg-primary`). Utiliza la función `url_for()` de Jinja2 para generar los enlaces dinámicos a las rutas del servidor.
- **Bloques Jinja2:** Incluye el bloque `{% block content %}` dentro de un contenedor `container-fluid` para integrar automáticamente el contenido específico de cada página.

### 3. Vistas y Plantillas Hijas (`templates/*.html`)
- **Herencia:** Las plantillas (`index.html`, `catalogo.html`, `servicios.html`, `contacto.html`) hacen uso de `{% extends "layout.html" %}` para reutilizar el diseño base.
- **Contenido particular:**
  - **`index.html`:** Muestra la bienvenida a la biblioteca escolar, su propósito y el horario de atención (7:00 a 15:00 de lunes a viernes).
  - **`catalogo.html`:** Presenta las categorías de materiales disponibles (libros, revistas, tesis y recursos digitales).
  - **`servicios.html`:** Detalla los servicios ofrecidos (préstamo, consulta en sala, recursos digitales y orientación) organizados mediante tarjetas (`cards`) de Bootstrap.
  - **`contacto.html`:** Muestra la dirección física, correo institucional ficticio y horarios de atención.

### 4. Estilos y Organización Visual
- **Bootstrap 5:** Se utilizó `container-fluid` para adaptar el contenido a todo el ancho disponible del navegador.
- **Diseño limpio:** Se aplicaron clases de utilidades de Bootstrap (`text-center`, `lead`, `bg-light`, `card`) para una presentación organizada y legible sin saturar la interfaz.
 
 