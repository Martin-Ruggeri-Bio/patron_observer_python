class Libro:
    def __init__(self, titulo="", estado=""):
        self._titulo = titulo
        self._estado = estado

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor
    
    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor