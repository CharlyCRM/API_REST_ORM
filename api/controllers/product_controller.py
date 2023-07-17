from flask import jsonify, request
from models.products import Producto
from db import session

'''Este fichero contiene las funciones API REST. Conectan con la base de datos y devuelven un JSON'''

#######
# GET #
#######
def getProducto(ref_producto):
    '''Realiza una consulta a la base de datos utilizando SQLAlchemy para obtener el producto correspondiente
    a la referencia proporcionada (ref_producto). Si se encuentra un producto con esa referencia, se devuelve un objeto JSON que contiene los detalles 
    del producto: como la referencia, el nombre, la descripción, el precio, la cantidad, la categoría, la fecha de fabricación y la imagen.
    Si no se encuentra ningún producto con la referencia proporcionada, se devuelve un objeto JSON con un mensaje indicando que el producto 
    no se encontró.'''
    producto_query = session.query(Producto).filter_by(ref_producto=ref_producto).first()
    if producto_query:
        return jsonify({
            'ref_producto': producto_query.ref_producto,
            'nombre': producto_query.nombre,
            'descripcion': producto_query.descripcion,
            'precio': producto_query.precio,
            'cantidad': producto_query.cantidad,
            'categoria': producto_query.categoria,
            'fecha_fabricacion': producto_query.fecha_fabricacion,
            'imagen': producto_query.imagen
            })
    return jsonify({
        'Mensaje': 'Producto no Encontrado'
    })
#------------------------------------------------------------------------------------------------------------------------------
########
# POST #
########
def postProducto():
    '''Recibe los datos del nuevo producto en formato JSON desde la solicitud HTTP. Se utilizan las claves del diccionario JSON para obtener 
    los valores correspondientes.
    A continuación, se crea una instancia de la clase Producto (objeto) con los datos recibidos y se verifica si la referencia del producto ya existe 
    en la base de datos. Si la referencia ya existe, se genera una excepción y se captura para devolver un mensaje de error indicando 
    que la referencia existe.'''
    try:
        # Obtengo los datos del nuevo producto del cuerpo de la solicitud JSON
        data = request.get_json() # indico que los datos recibidos desde el servidor vendrán en formato JSON

        ref_producto = data['ref_producto']
        nombre = data['nombre']
        descripcion = data['descripcion']
        precio = data['precio']
        cantidad = data['cantidad']
        categoria = data['categoria']
        fecha_fabricacion = data['fecha_fabricacion']
        imagen = data['imagen']

        # Creo una instancia (objeto) de Producto con los datos recibidos
        nuevo_producto = Producto(
            ref_producto=ref_producto,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            cantidad=cantidad,
            categoria=categoria,
            fecha_fabricacion=fecha_fabricacion,
            imagen=imagen
        )
        
        # Verifico si la ref_producto ya existe en la base de datos. Si ya existe capturo la execpcion con raise y la envio a Exception
        producto_existe = session.query(Producto).filter_by(ref_producto=ref_producto).first()
        if producto_existe:
            raise Exception('La ref_producto ya existe')
        
        # Agregar el nuevo objeto a la base de datos, tabla Producto
        session.add(nuevo_producto)
        session.commit()
        return jsonify({'mensaje': 'Producto agregado correctamente'})
    except KeyError:
        return jsonify({'mensaje': 'Error en los datos introducidos'})
    except Exception as e:
        return jsonify({'mensaje': f'Error en el servidor: {str(e)}'})
#----------------------------------------------------------------------------------------------------------------------
########
# PUT #
########
def putProducto(ref_producto):
    '''Recibe los datos actualizados del producto en formato JSON desde el cuerpo de la solicitud HTTP. Se utilizan las claves del diccionario JSON 
    para obtener los valores correspondientes.A continuación, se verifica si el producto con la referencia proporcionada existe en la tabla Producto 
    de la base de datos. Si el producto existe, se actualizan los datos del producto existente con los valores recibidos en la solicitud JSON. 
    Esto se realiza asignando los valores correspondientes a los atributos del objeto producto_existe.'''
    try:
        data = request.get_json()

        # Verifico si el producto existe en la tabla Producto
        producto_existe = session.query(Producto).filter_by(ref_producto=ref_producto).first()
        if producto_existe:
            # Actualizar los datos del producto existente con los valores recibidos en la solicitud JSON
            producto_existe.ref_producto = data['ref_producto']
            producto_existe.nombre = data['nombre']
            producto_existe.descripcion = data['descripcion']
            producto_existe.precio = data['precio']
            producto_existe.cantidad = data['cantidad']
            producto_existe.categoria = data['categoria']
            producto_existe.fecha_fabricacion = data['fecha_fabricacion']
            producto_existe.imagen = data['imagen']

            session.commit()
            return jsonify({'mensaje': 'Producto actualizado correctamente'})
        
        else:
            return jsonify({'mensaje': 'La ref_producto no existe'})
    
    except KeyError:
        return jsonify({'mensaje': 'Error en los datos introducidos'})
    except Exception as e:
        return jsonify({'mensaje': f'Error en el servidor: {str(e)}'})
#----------------------------------------------------------------------------------------------------------------------------------
##########
# DELETE #
#########
def deleteProducto(ref_producto):
    '''Verifica si el producto con la referencia proporcionada existe en la tabla Producto de la base de datos. Si el producto existe, 
        se utiliza la función delete de la sesión SQLAlchemy para eliminarlo de la base de datos.'''
    try:
        # Verifico si el producto existe en la tabla Producto
        producto_existe = session.query(Producto).filter_by(ref_producto=ref_producto).first()
        if producto_existe:
            session.delete(producto_existe)
            session.commit()
            
            return jsonify({'mensaje': 'Referencia eliminada correctamente'})

        else:
            return jsonify({'mensaje': 'La ref_producto no existe'})
        
    except KeyError:
        return jsonify({'mensaje': 'Error en los datos introducidos'})
    except Exception as e:
        return jsonify({'mensaje': f'Error en el servidor: {str(e)}'})



# GET = Método por defeto
# POST = Se usa para guardar datos
# PUT = Se usa para actualizar datos
# DELETE = Se usa para eliminar datos