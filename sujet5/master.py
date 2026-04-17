class Master:
    def __init__(self,nom):
        self._nom=nom

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    def __str__(self):
        return f"Master: {self._nom}\n "

if __name__ == "__main__":
    c = Master("Génie Logiciel et Systèmes Informatiques")
    print(c)