from subject import Subject


# Sujeto concreto
class AlarmaLibro(Subject):
    def __init__(self):
        self.observadores = []

    def attach(self, observer):
        self.observadores.append(observer)

    def detach(self, observer):
        self.observadores.remove(observer)

    def notifyObserver(self):
        for i in self.observadores:
            i.update()
