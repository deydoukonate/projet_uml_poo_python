class Eleve:
    def __init__(self,numero,nom,prenom,adresse,
                 dateNaissance):
        self._numero = numero
        self._nom = nom
        self._prenom = prenom
        self._adresse = adresse
        self._dateNaissance = dateNaissance

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

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
    def adresse(self):
        return self._adresse

    @adresse.setter
    def adresse(self, value):
        self._adresse = value

    @property
    def dateNaissance(self):
        return self._dateNaissance

    @dateNaissance.setter
    def dateNaissance(self, value):
        self._dateNaissance = value

    def __str__(self):
        return f"NUMERO: {self._numero}\n NOM: {self._nom}\n PRENOM: {self._prenom} \n ADRESSE: {self._adresse} \n DATE DE NAISSANCE: {self._dateNaissance}"

if __name__ == "__main__":
    e= Eleve(1, "Mairame", "Konate","cité avion","05/12/2001")
    print(e)    
