# CAMBIA ESTO:
INSTAGRAM_URL = "https://www.instagram.com/chili.delicemx/" 
# POR EJEMPLO:
INSTAGRAM_URL = "https://www.instagram.com/cchili.delicemx/"
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'clave_super_secreta_chili'  # Necesario para el carrito

# DATOS: Base de datos de productos
dulces = [
    {"id": 1, "nombre": "Trolli Sour Brite Crawlers", "precio": 60.00, "img": "/static/trolli.jpeg"},
    {"id": 2, "nombre": "Toxic Waste Red Sour Candy", "precio": 45.00, "img": "/static/toxicwaste.jpeg"},
    {"id": 3, "nombre": "Twizzlers STRAWBERRY", "precio": 85.00, "img": "/static/twizzlers.jpeg"},
    {"id": 4, "nombre": "Feastables Milk Crunch", "precio": 100.00, "img": "/static/feastables.jpeg"},
    {"id": 5, "nombre": "Prime Sabor Frambuesa", "precio": 60.00, "img": "/static/primef.jpeg"},
    {"id": 6, "nombre": "Prime Sabor ICE", "precio": 65.00, "img": "/static/primeice.jpeg"},
    {"id": 7, "nombre": "Pringles Múltiples Sabores", "precio": 95.00, "img": "/static/prin.jpeg"},
    {"id": 8, "nombre": "Peeps Múltiples Sabores", "precio": 145.00, "img": "/static/peeps.jpeg"},
    {"id": 9, "nombre": "Tropical Marshmallow", "precio": 40.00, "img": "/static/tropical.jpeg"},
    {"id": 10, "nombre": "Domes Sabor", "precio": 40.00, "img": "/static/domes.jpeg"}
]

# CONFIGURACIÓN: Tu Instagram para los pedidos
INSTAGRAM_URL = "https://www.instagram.com/chili.delicemx/"

@app.route('/')
def home():
    if 'carrito' not in session:
        session['carrito'] = []
    # Calculamos cantidad de items para mostrar en el icono del carrito
    cantidad_items = len(session['carrito'])
    return render_template('index.html', productos=dulces, cantidad_carrito=cantidad_items)

@app.route('/agregar/<int:id>')
def agregar_carrito(id):
    if 'carrito' not in session:
        session['carrito'] = []
    lista = session['carrito']
    lista.append(id)
    session['carrito'] = lista
    return redirect(url_for('home')) # Regresa al home para seguir comprando

@app.route('/carrito')
def ver_carrito():
    ids_carrito = session.get('carrito', [])
    productos_en_carrito = []
    total = 0
    
    for id_producto in ids_carrito:
        for dulce in dulces:
            if dulce['id'] == id_producto:
                productos_en_carrito.append(dulce)
                total += dulce['precio']
                break
    
    return render_template('carrito.html', items=productos_en_carrito, total=total, instagram_link=INSTAGRAM_URL)

@app.route('/vaciar')
def vaciar_carrito():
    session.pop('carrito', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)