from note import Note
#  Classe enfant 1
class NoteRapport(Note):
    def __init__(self, valeur, encadreur):
        super().__init__("Rapport", valeur)  
        self._encadreur = encadreur

    @property
    def encadreur(self):
        return self._encadreur

    @encadreur.setter
    def encadreur(self, value):
        self._encadreur = value

    def __str__(self):
        return f"{super().__str__()}, Encadreur: {self._encadreur}"


#  Classe enfant 2
class NoteDeSoutenance(Note):
    def __init__(self, valeur, jury):
        super().__init__("Soutenance", valeur) 
        self._jury = jury

    @property
    def jury(self):
        return self._jury

    @jury.setter
    def jury(self, value):
        self._jury = value

    def __str__(self):
        return f"{super().__str__()}, Jury: {self._jury}"


# je test pour voir
if __name__ == "__main__":
    r = NoteRapport(14.5, "Dr. Diallo")
    s = NoteDeSoutenance(16.0, "Mr. Mbaye")

    print(r)
    print(s)