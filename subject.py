from abc import abstractclassmethod
from iLibroMalEstado import ILibroMalEstado


class Subject():
    @abstractclassmethod
    def attach(self, observer: ILibroMalEstado):
        pass

    @abstractclassmethod
    def detach(self, observer: ILibroMalEstado):
        pass

    @abstractclassmethod
    def notifyObserver(self):
        pass
