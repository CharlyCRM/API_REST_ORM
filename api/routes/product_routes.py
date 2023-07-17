from flask import Blueprint, jsonify
from api.controllers.product_controller import getProducto, postProducto, putProducto, deleteProducto

'''Este fichero contiene las funciones vista relacionadas con Product_controller'''

producto_api = Blueprint('producto_api', __name__) # ver comentario de más abajo

#######
# GET #
#######
@producto_api.route('/producto/<string:ref_producto>', methods=['GET'])
def vista_getProducto(ref_producto):
    return getProducto(ref_producto)
#------------------------------------------------------------------------------------------------------------------
########
# POST #
########
@producto_api.route('/producto', methods=['POST'])
def vista_postProducto():
    return postProducto()
#--------------------------------------------------------------------------------------------------------------------
#######
# PUT #
#######
@producto_api.route('/producto/<string:ref_producto>', methods=['PUT'])
def vista_putProducto(ref_producto):
    return putProducto(ref_producto)
#------------------------------------------------------------------------------------------------------------------
##########
# DELETE #
#########
@producto_api.route('/producto/<string:ref_producto>', methods=['DELETE'])
def vista_deleteProducto(ref_producto):
    return deleteProducto(ref_producto)






'''Un blueprint es un objeto que nos permite organizar las rutas y las funciones relacionadas en módulos separados. 
Proporciona una forma de definir rutas y funciones en un archivo separado y luego registrar ese blueprint en la aplicación principal.
Un blueprint puede contener rutas, funciones de vista y cualquier otra lógica relacionada con una parte específica de una aplicación. 
Al registrar un blueprint en la aplicación principal, las rutas y las funciones del blueprint se incorporan a la aplicación y se pueden acceder 
y utilizar como cualquier otra ruta o función de vista.
Al utilizar blueprints, podemos dividir nuestra aplicación en módulos más pequeños y manejar diferentes partes de la aplicación de manera modular. 
Esto facilita la organización del código, el mantenimiento y la escalabilidad de la aplicación a medida que crece.

1-. Crea una variable que contenga la función Blueprint.
2.- Añade el decorador @nombre_variable para enlazar la función de vista y así poder ser ejecutada desde el fichero principal del programa (main.py)
'''