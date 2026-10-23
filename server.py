from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template(
        'index.html',
        titulo='Inicio',
        mensaje='Bienvenido a la Biblioteca Universitaria'
    )

@app.route('/catalogo')
def catalogo():
    return render_template(
        'catalogo.html',
        titulo='Catálogo General',
        mensaje='Explora nuestra amplia variedad de recursos de información y aprendizaje.'
    )

@app.route('/servicios')
def servicios():
    return render_template(
        'servicios.html',
        titulo='Nuestros Servicios',
        mensaje='Conoce los servicios que ofrecemos para apoyar tu formación académica e investigación.'
    )

@app.route('/contacto')
def contacto():
    return render_template(
        'contacto.html',
        titulo='Contacto',
        mensaje='Ponte en contacto con nuestro equipo para resolver tus dudas o solicitar asistencia.'
    )

if __name__ == '__main__':
    app.run(debug=True)