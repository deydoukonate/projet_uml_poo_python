class Projet:
    def __init__(self, id,nom,sujet,date):
        self._id = id
        self._nom = nom
        self._sujet = sujet
        self._date = date

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
    def sujet(self):
        return self._sujet

    @sujet.setter
    def sujet(self, value):
        self._sujet = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def __str__(self):
        return f"Identifiant: {self._id}\n Nom: {self._nom}\n   Sujet: {self._sujet}\n Date: {self._date}\n "

if __name__ == "__main__":
    p =Projet(10, "python","methode abstraite","16/05/2026")
    print(p)
