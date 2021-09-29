from alarmaLibro import AlarmaLibro
from compras import Compras
from administracion import Administracion
from stock import Stock
from libro import Libro
from biblioteca import Biblioteca


def main():
    # creo el sujeto concreto
    alarma = AlarmaLibro()

    # creamos los observadores concretos
    observerCompras = Compras()
    observerAdministracion = Administracion()
    observerStock = Stock()

    # cargamos una lista dinamica de observers que van a estar conectados
    alarma.attach(observerCompras)
    alarma.attach(observerAdministracion)
    alarma.attach(observerStock)

    # creamos un libro
    # libro = Libro("Caperucita", "BUENO")
    libro = Libro("Blanca Nieves", "MALO")

    # creamos una biblioteca
    biblioteca = Biblioteca(alarma)

    # devolvemos el libro
    biblioteca.devuelveLibro(libro)


'''
    Si el libro es bueno jamas se va a disparar la alarmaLibro
'''
if __name__ == '__main__':
    main()
