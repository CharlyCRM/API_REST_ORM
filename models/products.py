from sqlalchemy import Column, Integer, String, Boolean
from db import Base

class Producto(Base):
    '''Clase Producto -> Contiene los atributos de los productos de la tienda
        Args:
            ref_producto: Número de identificación del producto
            Nombre: El nombre del producto.
            Descripción: Una breve descripción del producto.
            Precio: El precio del producto.
            Cantidad: La cantidad disponible del producto en el inventario.
            Categoría: La categoría a la que pertenece el producto (por ejemplo, electrónica, ropa, alimentos, etc.).
            Fecha de fabricación: La fecha en que se fabricó el producto.
            imagen: nombre de la imagen asociada al producto'''
    
    __tablename__ = "producto"
    ref_producto = Column(Integer, primary_key = True)
    nombre = Column(String, nullable = True)
    descripcion = Column(String(500))
    precio = Column(Integer, nullable = True)
    cantidad = Column(Integer, nullable = True)
    categoria = Column(String(50),nullable = True)
    fecha_fabricacion = Column(String, nullable= True)
    imagen = Column(String(100), nullable= True)


    '''al utilizar el ORM de SQLAlchemy, no es necesario definir explícitamente los métodos getter y setter 
    para los atributos. SQLAlchemy los generará automáticamente. '''
    def __init__(self, ref_producto, nombre, descripcion, precio, cantidad, categoria, fecha_fabricacion, imagen): 
        self.ref_producto = ref_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        self.fecha_fabricacion = fecha_fabricacion
        self.imagen = imagen


    def __str__(self):
        return f"""
        Ref_producto: {self.ref_producto}
        Nombre: {self.nombre}
        Descripción: {self.descripcion}
        Precio: {self.precio}
        Cantidad: {self.cantidad}
        Categoria: {self.categoria}
        Fecha Fabricación: {self.fecha_fabricacion}
        Imagen: {self.imagen}"""


