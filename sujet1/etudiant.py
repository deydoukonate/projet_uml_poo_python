class Etudiant:
    def __init__(self, id, nom, prenom):
        self._id = id
        self._nom = nom
        self._prenom = prenom

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

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
        return f"Identifiant: {self._id}\n Nom: {self._nom}\n Prénom: {self._prenom}"

if __name__ == "__main__":
    e = Etudiant(2, "Deydou", "Konate")
    print(e)