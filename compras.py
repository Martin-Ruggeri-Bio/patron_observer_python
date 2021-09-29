from iLibroMalEstado import ILibroMalEstado


# observador concreto
class Compras(ILibroMalEstado):
    def update(self):
        print("Compras: ")
        print("Solicito cotización de reparación o reposición de libro...")
