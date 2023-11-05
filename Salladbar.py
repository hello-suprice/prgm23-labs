class Sallad:
    def __init__(self, namn=None, pris=None, ingredienser=None):
        self.namn = namn
        self.pris = pris if pris else 0
        self.ingredienser = set(ingredienser) if ingredienser else set()

    def matchar(self, valda_ingredienser):
        # Kontrollera om denna sallad matchar de valda ingredienserna
        return self.ingredienser == set(valda_ingredienser)

    def lägg_till_ingrediens(self, ingrediens):
        # Lägg till en ingrediens till denna sallad
        self.ingredienser.add(ingrediens.namn)
        self.pris += ingrediens.pris

    def ladda_sallader(self, filnamn):
    # Läs in sallader från fil och returnera en dictionary där nycklarna är salladnamnen
        with open(filnamn) as f:
            return {namn: Sallad(namn, pris, ingredienser.split()) for namn, pris, *ingredienser in (line.strip().split(',') for line in f)}

        
        


class Ingrediens:
    def __init__(self, namn, pris):
        self.namn = namn
        self.pris = pris

    def ladda_ingredienser(self, filnamn):
        # Läs in ingredienser från fil och returnera en dictionary där nycklarna är ingrediensnamnen
        with open(filnamn) as f:
            return {namn: Ingrediens(namn, pris) for namn, pris in (line.strip().split(',') for line in f)}


def välj_ingredienser():
    # Låt användaren välja ingredienser
    return input("Vilka ingredienser vill du ha i din sallad? (separera med kommatecken) ").split(',')

def hitta_matchande_sallader(sallader, valda_ingredienser):
    # Hitta matchande sallader baserat på valda ingredienser
    return [sallad for sallad in sallader if sallad.matchar(valda_ingredienser)]

def välj_extra_ingredienser(ingredienser):
    # Låt användaren välja extra ingredienser
    return input("Vilka extra ingredienser vill du lägga till? (separera med kommatecken) ").split(',')

def skriv_kvittot(sallad, filnamn):
    # Skriv ut kvitto till fil
    with open(filnamn, 'w') as f:
        f.write(f"Sallad: {sallad.namn}\n")
        f.write(f"Ingredienser: {', '.join(sallad.ingredienser)}\n")
        f.write(f"Totalt pris: {sallad.pris}\n")

def bearbeta_salladval(sallader, valda_ingredienser, ingredienser):
    matchande_sallader = hitta_matchande_sallader(sallader, valda_ingredienser)
    
    if matchande_sallader:
        # Visa alla matchande alternativ till användaren
        print("Här är de matchande salladerna:")
        for sallad in matchande_sallader:
            print(sallad.namn)
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
    sallad.ladda_sallader("sallader.txt")
    
    ingrediens = Ingrediens(None, None)
    ingrediens.ladda_ingredienser("ingredienser.txt")

    valda_ingredienser = välj_ingredienser()

    bearbeta_salladval(sallad, valda_ingredienser, ingrediens)

if __name__ == "__main__":
    main()