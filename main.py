from flask import Flask, render_template, request
from api.routes.product_routes import producto_api, vista_getProducto
import requests


app = Flask(__name__)

# Importa el blueprint producto_api, desde el directorio api/product_routes.py
app.register_blueprint(producto_api) 


@app.route('/')
def index():
    # Se obtiene el parametro ref_producto enviado desde la URL, Si el valor no está presente, por defecto se muestra **
    ref_producto = request.args.get('ref_producto', '111')
    # Se realiza una solicitud get a la ruta indicada
    respuesta = requests.get('http://127.0.0.1:5000/producto/' + ref_producto)
    # Se obtiene el contenido de la respuesta json y se guarda en una variable
    data = respuesta.json()
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
