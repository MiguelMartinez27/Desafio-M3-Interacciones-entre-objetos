class Producto:
    def __init__(self, nombre: str, precio: float, stock: int = 0):
        """
        Inicializa un nuevo producto con nombre, precio y stock.

        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        :param stock: Cantidad de stock disponible del producto. Si no se proporciona, se asume 0.
        """
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)  # El stock no puede ser menor a 0

    @property
    def nombre(self) -> str:
        """Obtiene el nombre del producto."""
        return self.__nombre

    @property
    def precio(self) -> float:
        """Obtiene el precio del producto."""
        return self.__precio

    @property
    def stock(self) -> int:
        """Obtiene el stock del producto."""
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock: int):
        """
        Modifica el stock del producto.

        :param nuevo_stock: Nuevo valor de stock. Si es menor que 0, se asigna 0.
        """
        self.__stock = max(0, nuevo_stock)

    def __eq__(self, otro) -> bool:
        """
        Compara dos productos por su nombre.

        :param otro: Otro producto a comparar.
        :return: True si tienen el mismo nombre, False en caso contrario.
        """
        return self.__nombre == otro.nombre

    def __add__(self, cantidad: int):
        """
        Suma una cantidad al stock del producto.

        :param cantidad: Cantidad a añadir al stock.
        :return: El producto con el stock actualizado.
        """
        self.stock += cantidad
        return self

    def __sub__(self, cantidad: int):
        """
        Resta una cantidad del stock del producto.

        :param cantidad: Cantidad a restar del stock.
        :return: El producto con el stock actualizado.
        """
        self.stock -= cantidad
        return self
