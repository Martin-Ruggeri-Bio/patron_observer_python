from abc import ABC, abstractclassmethod

class ILibroMalEstado(ABC):
    @abstractclassmethod
    def update(self):
        pass
    