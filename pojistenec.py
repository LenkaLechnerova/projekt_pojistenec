class Pojistenec:
    """ Vytvoření třídy pojištěných osob."""

    """Kostruktor pro inicializaci pojištěné osoby, její jméno, příjmení, věk a telefon."""
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    """ Výpis textové podoby."""
    def __str__(self):
        return (f"{self.jmeno} {self.prijmeni} {self.vek} {self.telefon}")





    