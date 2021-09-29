from iLibroMalEstado import ILibroMalEstado


# observador concreto
class Administracion(ILibroMalEstado):
    def update(self):
        print("Administracion: ")
        print("Suspensión de socio")
        print("Hasta la reposición o reparación del daño causado...")
