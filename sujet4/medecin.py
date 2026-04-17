from personne import Personne
#  Classe enfant 2
class Medecin(Personne):
    def __init__(self,grade):
        self._grade=grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    def __str__(self):
        return f"Grade: {self._grade}"

if __name__ == "__main__":
    m= Medecin("Medecin generaliste")
    print(m)   