from evidence import Evidence
import os


""" Kontrola zadání výběru akce - od 1 do 4. """
def nacti_akci(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            cislo = int(input(text_zadani))
            if cislo >0 and cislo <5:
                spatne = False
        except ValueError:
            print(text_chyba)
    else:
        return cislo 

""" Výpis a výběr akce pro evidenci pojištěných osob. """
def main():
    volba = 1
    evidence = Evidence()
    """ Pokud je volba 4, program se ukončí, jinak nabídne výběr. """
    while volba != 4:
        os.system("cls")  # vyčistím
        print("-------------------------------")
        print("Evidence pojištěných osob")
        print("-------------------------------")
        print()
        print("Klíč pro výběr akce:")
        print("1 - Přidat nového pojištěnce")
        print("2 - Vypsat všechny pojištěnce")
        print("3 - Vyhledat pojištěnce")
        print("4 - Konec")

        print()
        volba = nacti_akci("Vaše volba je: ", "Neplatné číslo!")
        print()
        
        """ Volba 1 - přidání nového pojištěnce. """
        if volba == 1:
            evidence.pridej_pojistence()
            print()
            pokracovat = input("Data byla uložena. Pokračujte libovolnou klávesou...")
        
            """ Volba 2 - výpis všech pojištěnců. """
        elif volba == 2:
            evidence.vypis_vsech_pojistencu()
            print()
            pokracovat = input("Pokračujte libovolnou klávesou...")

            """ Volba 3 - vyhledání vloženého pojištěnce. """
        elif volba == 3:
            evidence.vyber_jednoho_pojistence()
            print()
            pokracovat = input("Pokračujte libovolnou klávesou...")

    print()
    print("Děkujeme za použití evidence pojištěných osob.")
    print()



""" Spustí se program pro evidenci osob. """
main()
