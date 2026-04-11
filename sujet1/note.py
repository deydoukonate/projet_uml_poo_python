class Note:
    def __init__(self ,type,valeur):
        self._type = type
        self._valeur = valeur
        

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def valeur(self):
        return self._valeur

    @valeur.setter
    def valeur(self, value):
        self._valeur = value

    def __str__(self):
        return f"Type: {self._type}\n Valeur: {self._valeur}\n "

if __name__ == "__main__":
    n =Note("suffissant", 12.5)
    print(n)
