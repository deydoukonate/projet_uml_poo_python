class Question:
    def __init__(self,intitule,reponse,niveau,theme):
        self._intitule=intitule
        self._reponse=reponse
        self._niveau=niveau
        self._theme=theme

    @property
    def intitule(self):
        return self._intitule

    @intitule.setter
    def intitule(self, value):
        self._intitule = value

    @property
    def reponse(self):
        return self._reponse

    @reponse.setter
    def reponse(self, value):
        self._reponse = value

    @property
    def niveau(self):
        return self._niveau

    @niveau.setter
    def niveau(self, value):
        self._niveau = value

    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, value):
        self._theme = value

    def __str__(self):
        return f"Intitule: {self._intitule}\n Réponse: {self._reponse}\n Resultat: {self._niveau}\n Theme: {self._theme}"

if __name__ == "__main__":
    q=Question( "les base de l'algorithme"," important pour le dev","resoudre des probleme","Algorithme")
    print(q)    