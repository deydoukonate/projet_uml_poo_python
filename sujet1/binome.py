class Binome:
    def __init__(self, numero,date):
        self._numero = numero
        self._date = date


    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def __str__(self):
        return f"Identifiant: {self._numero}\n Nom: {self._date}\n "

if __name__ == "__main__":
    b =Binome(6, "15/04/2026")
    print(b)