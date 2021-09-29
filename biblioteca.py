'''Esta clase copera con el sistema con un metodo que va a recibir un libro
Si el libro esta malo disparo el patron observador'''


class Biblioteca:
    def __init__(self, alarma):
        self._alarma = alarma

    @property
    def alarma(self):
        return self._alarma

    @alarma.setter
    def alarma(self, valor):
        self._alarma = valor

    def devuelveLibro(self, libro):
        if libro.estado == "MALO":
            self.alarma.notifyObserver()
