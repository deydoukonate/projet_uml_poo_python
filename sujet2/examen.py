class Examen:
    def __init__(self,dateExamen,nbFaute,resultat):
        self._dateExamen=dateExamen
        self._nbFaute=nbFaute
        self._resultat=resultat

    @property
    def dateExamen(self):
        return self._dateExamen

    @dateExamen.setter
    def dateExamen(self, value):
        self._dateExamen = value

    @property
    def nbFaute(self):
        return self._nbFaute

    @nbFaute.setter
    def nbFaute(self, value):
        self._nbFaute = value

    @property
    def resultat(self):
        return self._resultat

    @resultat.setter
    def resultat(self, value):
        self._resultat = value

    def __str__(self):
        return f"Date Examen: {self._dateExamen}\n nombres de fautes: {self._nbFaute}\n Resultat: {self._resultat}"

if __name__ == "__main__":
    e= Examen( "18/05/2026","4","oui")
    print(e)    
