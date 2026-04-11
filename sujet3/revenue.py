class Revenue:
    def __init__(self,nom,redacteur,frequence):
        self._nom=nom
        self._redacteur=redacteur
        self._frequence=frequence


    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def redacteur(self):
        return self._redacteur

    @redacteur.setter
    def redacteur(self, value):
        self._redacteur = value

    @property
    def frequence(self):
        return self._frequence

    @frequence.setter
    def frequence(self, value):
        self._frequence = value

    def __str__(self):
        return f"NOM DU REVENU: {self._nom}\n REDACTEUR DU REVENU: {self._redacteur}\n FREQUENCE DU REVENU: {self._frequence}\n"
    
if __name__ == "__main__":
    r= Revenue("Salaire","Employeur","Mensuelle")
    print(r)    
