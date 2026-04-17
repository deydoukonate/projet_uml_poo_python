class Cour:
    def __init__(self,intitule):
        self._intitule=intitule


    @property
    def intitule(self):
        return self._intitule

    @intitule.setter
    def intitule(self, value):
        self._intitule = value

    def __str__(self):
        return f"Intitule: {self._intitule}\n "

if __name__ == "__main__":
    c =Cour("reference digital")
    print(c)