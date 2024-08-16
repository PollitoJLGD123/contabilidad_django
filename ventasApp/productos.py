class Product:
    def __init__(self, numero, descripcion, categoria, cantidad, preciounitario, preciototal):
        self._numero = numero
        self._descripcion = descripcion
        self._categoria = categoria
        self._cantidad = cantidad
        self._preciounitario = preciounitario
        self._preciototal = preciototal
    
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        self._numero = valor

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        self._categoria = valor

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        self._cantidad = valor

    @property
    def preciounitario(self):
        return self._preciounitario

    @preciounitario.setter
    def preciounitario(self, valor):
        self._preciounitario = valor

    @property
    def preciototal(self):
        return self._preciototal
    
    @preciototal.setter
    def preciototal(self, valor):
        self._preciototal = valor
