class Sallad:
    def __init__(self, namn, pris, ingredienser):
        self.namn = namn
        self.pris = pris
        self.ingredienser = ingredienser

    def matchar(self, valda_ingredienser):
        # Kontrollera om denna sallad matchar de valda ingredienserna
        pass

    def lägg_till_ingrediens(self, ingrediens):
        # Lägg till en ingrediens till denna sallad
        pass

    def ladda_sallader(self, filnamn):
        # Läs in sallader från fil och returnera en dictionary där nycklarna är salladnamnen
        pass

class Ingrediens:
    def __init__(self, namn, pris):
        self.namn = namn
        self.pris = pris

    def ladda_ingredienser(self, filnamn):
        # Läs in ingredienser från fil och returnera en dictionary där nycklarna är ingrediensnamnen
        pass

def välj_ingredienser():
    # Låt användaren välja ingredienser
    pass

def hitta_matchande_sallader(sallader, valda_ingredienser):
    # Hitta matchande sallader baserat på valda ingredienser
    pass

def välj_extra_ingredienser(ingredienser):
    # Låt användaren välja extra ingredienser
    pass

def skriv_kvittot(sallad, filnamn):
    # Skriv ut kvitto till fil
    pass

def bearbeta_salladval(sallader, valda_ingredienser, ingredienser):
    matchande_sallader = hitta_matchande_sallader(sallader, valda_ingredienser)
    
    if matchande_sallader:
        # Visa alla matchande alternativ till användaren
        pass
    else:
        närmaste_sallad = min(sallader, key=lambda sallad: len(set(valda_ingredienser) - set(sallad.ingredienser)))

        extra_ingredienser = välj_extra_ingredienser(ingredienser)
        
        for ingrediens_namn in extra_ingredienser:
            ingrediens = next((i for i in ingredienser if i.namn == ingrediens_namn), None)
            if ingrediens:
                närmaste_sallad.lägg_till_ingrediens(ingrediens)

        skriv_kvittot(närmaste_sallad, "kvitto.txt")

def main():
    sallad = Sallad(None, None, None)
    sallader = sallad.ladda_sallader("sallader.txt")
    
    ingrediens = Ingrediens(None, None)
    ingredienser = ingrediens.ladda_ingredienser("ingredienser.txt")

    valda_ingredienser = välj_ingredienser()

    bearbeta_salladval(sallader, valda_ingredienser, ingredienser)

if __name__ == "__main__":
    main()