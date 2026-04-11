class Article:
    def __init__(self,titre,contenu):
        self._titre=titre
        self._contenu=contenu

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, value):
        self._titre = value

    @property
    def contenu(self):
        return self._contenu

    @contenu.setter
    def contenu(self, value):
        self._contenu = value
    def __str__(self):
        return f"TITRE: {self._titre}\n CONTENU: {self._contenu}\n "
    
if __name__ == "__main__":
    a= Article("L'augmentation des revenue en 2026","En 2026 plusieur secteurs ont connu,une hausse notable de leurs revenus. Cette progression, estimée à environ +15 %, s’explique par une amélioration des conditions économiques et une forte demande sur le marché. Les entreprises ont ainsi pu augmenter leurs performances et offrir de meilleures opportunités d’emploi. Toutefois, certains défis persistent, notamment la gestion des coûts et la stabilité des prix. Malgré cela, les perspectives restent encourageantes pour le reste de l’année")
    print(a)    
