class Auteur:
    def __init__(self,nom,prenom,numeroCarte):
       self._nom=nom
       self._prenom=prenom
       self._numeroCarte=numeroCarte


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
    def numeroCarte(self):
        return self._numeroCarte

    @numeroCarte.setter
    def numeroCarte(self, value):
        self._numeroCarte = value

    def __str__(self):
        return f"NOM AUTEUR: {self._nom}\n : {self._prenom}\n PRENOM DE L AUTEUR : {self._prenom}\n SON NUMERO DE CARTE PROFESSIONNELLE : {self._numeroCarte}\n "
    
if __name__ == "__main__":
    a= Auteur("Absa","NDIANG","CP_2026_001245")
    print(a)  
