from personne import Personne

    #  Classe enfant 1
class Assure(Personne):
    def __init__(self,numSecuriteSociale):
        self._numSecuriteSociale=numSecuriteSociale

    @property
    def numSecuriteSociale(self):
        return self._numSecuriteSociale

    @numSecuriteSociale.setter
    def numSecuriteSociale(self, value):
        self._numSecuriteSociale = value

    def __str__(self):
        return f"NUMERO DE SECURITE SOCIALE/{self._numSecuriteSociale}"
    
if __name__ == "__name__" :
    a=Assure("1 85 125 46 96 3 5 47 10")
    print(a)