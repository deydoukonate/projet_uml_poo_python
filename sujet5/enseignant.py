class Enseignant:
    def __init__(self,numen,nom,prenom):
        self._numen=numen
        self._nom=nom
        self._prenom=prenom
     

    @property
    def numen(self):
        return self._numen

    @numen.setter
    def numen(self, value):
        self._numen = value

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
    def __str__(self):
        return f"Numen: {self._numen}\n Nom: {self._nom}\n Prenom: {self._prenom} "

if __name__ == "__main__":
    e =Enseignant(6, "Sidy","diop")
    print(e)