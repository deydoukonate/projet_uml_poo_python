class Consultation:
    def __init__(self,date,motif,ordonnance):
       self._date=date
       self._motif=motif
       self._ordonnance=ordonnance



    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def motif(self):
        return self._motif

    @motif.setter
    def motif(self, value):
        self._motif = value

    @property
    def ordonnance(self):
        return self._ordonnance

    @ordonnance.setter
    def ordonnance(self, value):
        self._ordonnance = value

    def __str__(self):
        return f"Grade: {self._date}\n  {self._motif}\n  {self._ordonnance}\n"

if __name__ == "__main__":
    c= Consultation("14 avril 2026", "fièvre et maux de tête depuis 2jr","Amoxilline 1g, Paracétamol 500mg")
    print(c)