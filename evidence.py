from pojistenec import Pojistenec

class Evidence:
    """ Vytvoření třídy evidence pro pojištěné osoby."""

    """Kostruktor pro inicializaci seznamu pojištěnců. """
    def __init__(self):
        self.seznam_pojistencu = []

    """ Metoda pro přidání nového pojištěnce. Automatická oprava - jméno a příjmení s prvním velkým písmenem, kontrola zadání věku od 0 do 120 let a kontrola telefonního čísla (9 číslic)."""
    def pridej_pojistence(self):

        """ Zadání jména a příjmení. """
        jmeno = input("Zadejte jméno pojištěného:\n").capitalize()
        prijmeni = input("Zadejte příjmení pojištěného:\n").capitalize()

        """ Zadání a kontrola věku. """
        spatne = True
        while spatne:
            vek = input("Zadejte věk pojištěného:\n")
            if int(vek) < 0 or int(vek) > 120:
                print("Chybně zadaný věk (věk není v očekávaném rozmezí).")
            elif vek.isdigit() != True:
                print("Chybně zadaný věk (věk obsahuje písmeno).")
            else:
                spatne = False

        """ Zadání a kontrola telefonního čísla. """
        spatne = True
        while spatne:
            telefon = input("Zadejte telefonní číslo pojištěného:\n")
            if len(telefon) != 9:
                print("Chybně zadané telefonní číslo: zadejte 9 číslic (číslo je moc krátké či dlouhé).")
            elif telefon.isdigit() != True:
                print("Chybně zadané telefonní číslo: zadejte 9 číslic (číslo obsahuje písmeno).")
            else:
                spatne = False
    
        """ Vloží zadané vstupy do objektu novy_pojistenec."""
        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
       # novy_pojistenec = str(novy_pojistenec)
        self.seznam_pojistencu.append(novy_pojistenec)
        return (self.seznam_pojistencu)     


    """ Metoda pro vypsání osob z evidence pojištěných."""
    def vypis_vsech_pojistencu(self):
        if self.seznam_pojistencu == []:
                print("Seznam je prázdný. Nejprve vložte pojištěnce.")
        else:
            for i in self.seznam_pojistencu:
                rozdeleni = str(i).split()
                for j in rozdeleni:
                    print(j, "\t", end=" ")
                print()


    """ Metoda pro výběr pojištěného přes jméno a příjmení - jméno a příjmení s prvním velkým písmenem. """
    def vyber_jednoho_pojistence(self):
        vyber_jmeno = input("Zadejte jméno pojištěného:\n").capitalize()
        vyber_prijmeni = input("Zadejte příjmení pojištěného:\n").capitalize()
        print()
        for i in self.seznam_pojistencu:
            rozdeleni = str(i).split()
            if vyber_jmeno in rozdeleni[0]:
                if vyber_prijmeni in rozdeleni[1]:
                    for j in rozdeleni:
                        print(j, "\t", end=" ")
                else:
                    print("Hledaná osoba nebyla nalezena. Zkuste to znovu.")
            else:
                print("Hledaná osoba nebyla nalezena. Zkuste to znovu.")
        print()