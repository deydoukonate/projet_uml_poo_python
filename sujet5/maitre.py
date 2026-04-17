from enseignant import Enseignant
class Maitre(Enseignant):
   def __init__(self,numen,nom,prenom,titrethese):
    super().__init__(numen,nom,prenom)
    self._titrethese=titrethese 

    @property
    def titrethese(self):
        return self._titrethese

    @titrethese.setter
    def titrethese(self, value):
        self._titrethese = value

    def __str__(self):
        return f"{super().__str__()}, TITRE THESE: {self._titrethese}"


if __name__ == "__main__":
    b = Maitre(6,"Dupont","Jean","Intelligence Artificielle et Apprentissage Automatique")
    print(b)