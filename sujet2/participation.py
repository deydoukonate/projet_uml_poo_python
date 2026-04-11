class Participation:
    def __init__(self,nbFaute):
        self._nbFaute=nbFaute


    @property
    def nbFaute(self):
        return self._nbFaute

    @nbFaute.setter
    def nbFaute(self, value):
        self._nbFaute = value


    def __str__(self):
        return f" Nombre de faute: {self._nbFaute}"

if __name__ == "__main__":
    p= Participation( "05")
    print(p)    