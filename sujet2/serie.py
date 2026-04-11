class Serie:
    def __init__(self,numero,):
        self._numero=numero

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    def __str__(self):
        return f"NUMERO: {self.numero}"

if __name__ == "__main__":
    s= Serie( 5)
    print(s)    