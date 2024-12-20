from Animal import Animal

class Gato(Animal):
    _totalCreados = 0
    
    def __init__(self, nombre, edad, raza, pelaje):
        super.__init__(nombre, edad, raza)
        self._pelaje = pelaje
        Gato._totalCreados += 1
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    
    def getPelaje(self):
        return self._pelaje
    
    def caminar(self):
        return "se mueve lentamente"
    
    def correr(self):
        return "salta al punto"
    
    def ruido(self):
        print("miau")
    
    @classmethod
    def getTotalCreados(cls):
        return cls._totalCreados 