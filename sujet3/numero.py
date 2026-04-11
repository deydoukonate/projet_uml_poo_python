class Numero:
    def __init__(self,nbRelative,anneeEnCour):
        self._nbRelative=nbRelative
        self._anneeEnCour=anneeEnCour
        

    @property
    def nbRelative(self):
        return self._nbRelative

    @nbRelative.setter
    def nbRelative(self, value):
        self._nbRelative = value

    @property
    def anneeEnCour(self):
        return self._anneeEnCour

    @anneeEnCour.setter
    def anneeEnCour(self, value):
        self._anneeEnCour = value

    def __str__(self):
        return f"NOMBRE RELATIF: {self._nbRelative}\n ANNEE EN COUR: {self._anneeEnCour}\n "
    
if __name__ == "__main__":
    n= Numero("+15%","2026")
    print(n)    
