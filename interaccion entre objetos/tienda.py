from producto import Producto
from abc import ABC, abstractmethod


class Tienda(ABC):
    def __init__(self, nombre: str, costo_delivery: float):
        """
        Inicializa una nueva tienda con un nombre y costo de delivery.

        :param nombre: Nombre de la tienda.
        :param costo_delivery: Costo del servicio de delivery.
        """
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self._productos = []

    @property
    def nombre(self) -> str:
        """Obtiene el nombre de la tienda."""
        return self.__nombre

    @property
    def costo_delivery(self) -> float:
        """Obtiene el costo de delivery de la tienda."""
        return self.__costo_delivery

    @abstractmethod
    def ingresar_producto(self, nombre: str, precio: float, stock: int):
        """Ingresa un producto a la tienda."""
        pass

    @abstractmethod
    def listar_productos(self) -> str:
        """Lista los productos de la tienda."""
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto: str, cantidad: int):
        """Realiza una venta en la tienda."""
        pass


class Restaurante(Tienda):
    def ingresar_producto(self, nombre: str, precio: float, stock: int):
        producto = Producto(nombre, precio, 0)  # Los productos siempre tienen stock 0
        for p in self._productos:
            if p == producto:
                return  # No modifica el producto existente

        self._productos.append(producto)

    def listar_productos(self) -> str:
        return "\n".join([f"Producto: {p.nombre}, Precio: {p.precio}" for p in self._productos])

    def realizar_venta(self, nombre_producto: str, cantidad: int):
        # No se modifica el stock en restaurantes.
        pass


class Supermercado(Tienda):
    def ingresar_producto(self, nombre: str, precio: float, stock: int):
        producto = Producto(nombre, precio, stock)
        for p in self._productos:
            if p == producto:
                p + stock
                return
        self._productos.append(producto)

    def listar_productos(self) -> str:
        listado = []
        for p in self._productos:
            detalle = f"Producto: {p.nombre}, Precio: {p.precio}, Stock: {p.stock}"
            if p.stock < 10:
                detalle += " - Pocos productos disponibles"
            listado.append(detalle)
        return "\n".join(listado)

    def realizar_venta(self, nombre_producto: str, cantidad: int):
        for p in self._productos:
            if p.nombre == nombre_producto:
                cantidad_vendida = min(cantidad, p.stock)
                p - cantidad_vendida
                break


class Farmacia(Tienda):
    def ingresar_producto(self, nombre: str, precio: float, stock: int):
        producto = Producto(nombre, precio, stock)
        for p in self._productos:
            if p == producto:
                p + stock
                return
        self._productos.append(producto)

    def listar_productos(self) -> str:
        listado = []
        for p in self._productos:
            detalle = f"Producto: {p.nombre}, Precio: {p.precio}, Stock: {p.stock}"
            if p.precio > 15000:
                detalle += " - Envío gratis al solicitar este producto"
            listado.append(detalle)
        return "\n".join(listado)
                
    def realizar_venta(self, nombre_producto: str, cantidad: int):
        if cantidad > 3:
            return  print("No se puede vender más de 3")
        for p in self._productos:
            if p.nombre == nombre_producto:
                cantidad_vendida = min(cantidad, p.stock)
                p - cantidad_vendida
                break
