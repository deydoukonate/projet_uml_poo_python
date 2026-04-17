from enseignant import Enseignant

class Professeur(Enseignant):
    def __init__(self, numen, nom, prenom,titreHDR):
        super().__init__(numen, nom, prenom )
        self._titreHDR = titreHDR

    @property
    def titreHDR(self):
        return self._titreHDR

    @titreHDR.setter
    def titreHDR(self, value):
        self._titreHDR = value

    def __str__(self):
        return f"{super().__str__()}, TITRE HDR: {self._titreHDR}"


if __name__ == "__main__":
    b = Professeur(1,"Martin","Sophie","Systèmes Distribués et Réseaux Intelligents" )
    print(b)