class Formation:
    def __init__(self,id,nom,promotion):
        self._id=id
        self._nom=nom
        self._promotion=promotion


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
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, value):
        self._promotion = value
    
    def __str__(self):
        return f"Identifiant:{self. _id}\n Nom:{self._nom}\n Promotion:{self._promotion}\n "

if __name__ == "__main__":
    f = Formation(1, "MIAGE-IF", "Initiale")
    print(f)