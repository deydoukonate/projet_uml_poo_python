class Cdrom:
    def __init__(self,numero,numEditeur):
        self._numero=numero
        self._numEditeur=numEditeur

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def numEditeur(self):
        return self._numEditeur

    @numEditeur.setter
    def numEditeur(self, value):
        self._numEditeur = value

    def __str__(self):
        return f"NUMERO: {self.numero}\n NOM DE L EDITEUR: {self._numEditeur}"

if __name__ == "__main__":
    c= Cdrom( 3,"google chrome")
    print(c)    