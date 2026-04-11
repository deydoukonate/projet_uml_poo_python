class Seance:
    def __init__(self,dateSeance, heureSeance):
        self._dateSeance=dateSeance
        self._heureSeance = heureSeance

    @property
    def dateSeance(self):
        return self._dateSeance

    @dateSeance.setter
    def dateSeance(self, value):
        self._dateSeance = value

    @property
    def heureSeance(self):
        return self._heureSeance

    @heureSeance.setter
    def heureSeance(self, value):
        self._heureSeance = value
    def __str__(self):
        return f"Date: {self._dateSeance}\n Heur: {self._heureSeance}"

if __name__ == "__main__":
    s= Seance( "15/01/2004","09h: 30mn", )
    print(s)    

        