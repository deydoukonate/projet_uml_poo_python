class Personne :
    def __init__(self,nom,prenom,dateNaissance,adresse):
        self._nom=nom
        self._prenom=prenom
        self._dateNaissanace=dateNaissance
        self._adresse=adresse


    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value

    @property
    def dateNaissanace(self):
        return self._dateNaissanace

    @dateNaissanace.setter
    def dateNaissanace(self, value):
        self._dateNaissanace = value

    @property
    def adresse(self):
        return self._adresse

    @adresse.setter
    def adresse(self, value):
        self._adresse = value

def __str__(self):
        return f"NOM: {self._nom}\n PRENOM: {self._prenom} \n DATE DE NAISSANCE: {self._dateNaissance}\n ADRESSE: {self._adresse}"
    
if __name__ == "__name__" :
    p=Personne("DIALLO","Khalil","08/10/2002","Dakar")
    print(p)
