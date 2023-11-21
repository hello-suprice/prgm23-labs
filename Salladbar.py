import json 

class Ingrediens:
    '''
    Representerar en ingrediens med namn och pris.
    '''
    def __init__(self, namn_ingrediens, ingrediens_pris):
        self.namn_ingrediens = namn_ingrediens
        self.ingrediens_pris = ingrediens_pris

    def __str__(self):
        return f"{self.namn_ingrediens} ({self.ingrediens_pris} kr)"

class Sallad:
    def __init__(self, namn_sallad, sallad_pris, ingredienser):
        self.namn_sallad = namn_sallad
        self.sallad_pris = sallad_pris
        self.ingredienser = ingredienser 

    def __str__(self):
        ingredienser_str = ', '.join(str(ingrediens) for ingrediens in self.ingredienser)
        return f"{self.namn_sallad} ({self.sallad_pris} kr): {ingredienser_str}" 

class Salladbar():

    def __init__(self):
        self.sallader = []
        self.ingredienser = []
    
    def läs_in_sallader(self):
        """
        Läser in sallader från en JSON-fil och lagrar dem i en lista.
        """
        try:
            with open('sallader.json', 'r', encoding='utf-8') as f:
                sallader_data = json.load(f)
                for sallad_data in sallader_data:
                    namn_sallad = sallad_data["namn_sallad"]
                    sallad_pris = sallad_data["sallad_pris"]
                    ingredienser = sallad_data["ingredienser"]
                    self.sallader.append(Sallad(namn_sallad, sallad_pris, ingredienser))
        except FileNotFoundError:
            print("Kunde inte hitta filen 'sallader.json'. Kontrollera att filen finns och försök igen.")
        
    def läs_in_ingredienser(self):
        """
        Läser in ingredienser från en JSON-fil och lagrar dem i en lista.
        """
        try:
            with open('ingredienser.json', 'r', encoding='utf-8') as f:
                ingredienser_data = json.load(f)
                for ingrediens_data in ingredienser_data:
                    namn_ingrediens = ingrediens_data["namn_ingrediens"]
                    ingreidens_pris = ingrediens_data["ingrediens_pris"]
                    self.ingredienser.append(Ingrediens(namn_ingrediens, ingreidens_pris))
        except FileNotFoundError:
            print("Kunde inte hitta filen 'ingredienser.json'. Kontrollera att filen finns och försök igen.")

    def välj_ingredienser(self):
        """
        Låter användaren välja ingredienser för sin sallad.
        """
        print("Välj dina ingredienser:")
        for i, ingrediens in enumerate(self.ingredienser, start=1):   # https://www.geeksforgeeks.org/enumerate-in-python/
            print(f"{i}. {ingrediens}")
        while True:

            valda_nummer = input().split(',')
            try: 
                for nummer in valda_nummer:
                    if not nummer.isdigit() or not 1 <= int(nummer) <= len(self.ingredienser):
                        raise ValueError
                break
            except ValueError:
                print("Ogiltigt inmatning. Ange numren för dina valda ingredienser, separerade med kommatecken.")
        
        
        valda_ingredienser = [ingrediens for i, ingrediens in enumerate(self.ingredienser, start=1) if str(i) in valda_nummer]
        return valda_ingredienser


    def hitta_matchande_sallader(self, valda_ingredienser):
        """
        Hittar alla sallader som matchar de valda ingredienserna.
        """
        

        valda_ingredienser_namn = [ingrediens.namn_ingrediens for ingrediens in valda_ingredienser]
        '''
        # Kontrollera om de valda ingredienserna finns i alla sallader
        for sallad in self.sallader:
            if not set(valda_ingredienser_namn).issubset(set(sallad.ingredienser)):
                break
        else:
            print("Du har valt ingredienser som finns i alla sallader. Det finns ingen bästa matchande sallad.")
            return None, None, None
        '''
        perfekta_matchningar = [sallad for sallad in self.sallader if set(valda_ingredienser_namn) == set(sallad.ingredienser)]

        if perfekta_matchningar:
            print("Här är salladerna som matchar dina valda ingredienser:")
            for sallad in perfekta_matchningar:
                print(sallad)
            total_pris = perfekta_matchningar[0].sallad_pris  # Priset för den perfekta matchningen
            return perfekta_matchningar, None, total_pris


        else:
            bästa_match = None
            bästa_match_antal = 0
            bästa_match_pris = float('inf')   
            bästa_match_kompletterande_ingredienser = None
            for sallad in self.sallader:
                matchande_ingredienser = set(valda_ingredienser_namn).intersection(set(sallad.ingredienser))
                kompletterande_ingredienser = set(sallad.ingredienser) - set(valda_ingredienser_namn)
                kompletterande_pris = sum([ingrediens.ingrediens_pris for ingrediens in self.ingredienser if ingrediens.namn_ingrediens in kompletterande_ingredienser])
                if len(matchande_ingredienser) > bästa_match_antal or (len(matchande_ingredienser) == bästa_match_antal and sallad.sallad_pris + kompletterande_pris < bästa_match_pris and not kompletterande_ingredienser):
                    bästa_match = sallad
                    bästa_match_antal = len(matchande_ingredienser)
                    bästa_match_pris = sallad.sallad_pris + kompletterande_pris
                    bästa_match_kompletterande_ingredienser = kompletterande_ingredienser

            print(f"Bästa matchande sallad är {bästa_match.namn_sallad} med priset {bästa_match.sallad_pris} kr.")
            print(f"Du kan lägga till dessa ingredienser: {', '.join(bästa_match_kompletterande_ingredienser)}")

            while True:
                svar = input("Vill du lägga till de kompletterande ingredienserna? (ja/nej) ")
                if svar.lower() == 'ja':
                    print(f"Totalkostnaden blir {bästa_match_pris} kr.")
                    return [bästa_match], bästa_match_kompletterande_ingredienser, bästa_match_pris
                elif svar.lower() == 'nej':
                    valda_ingredienser_pris = sum(ingrediens.ingrediens_pris for ingrediens in valda_ingredienser)
                    print(f"Totalkostnaden blir {valda_ingredienser_pris} kr.")
                    return [bästa_match], None, valda_ingredienser_pris
                else:
                    print("Skriv ett lämpligt svar ja eller nej!")


    def välj_extra_ingredienser(self):
        """
        Låter användaren välja extra ingredienser.
        """
        print("Här är alla tillgängliga ingredienser och deras priser:")
        for i, ingrediens in enumerate(self.ingredienser, start=1):
            print(f"{i}. {ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr")

        extra_ingredienser = []
        val = input("Välj ingredienser att lägga till genom att ange deras nummer, separerade med kommatecken, eller skriv 'klar' när du är färdig: ")
        if val.lower() != 'klar':
            valda_nummer = val.split(',')
            for nummer in valda_nummer:
                if nummer.isdigit() and 1 <= int(nummer) <= len(self.ingredienser):
                    extra_ingredienser.append(self.ingredienser[int(nummer) - 1])
                else:
                    print(f"Ogiltigt val: {nummer}. Försök igen.")

        return extra_ingredienser

    def skriv_kvittot(self, valda_ingredienser, extra_ingredienser, total_pris, bästa_match=None, kompletterande_ingredienser=None):
        """
        Skriver ut ett kvitto med de valda ingredienserna, eventuella extra ingredienser, och det totala priset.
        """
        print("Här är ditt kvitto:")
        print("""
              Valda ingredienser:
              """)
        for ingrediens in valda_ingredienser:
            print(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr")
    
        if extra_ingredienser:
            print("Extra ingredienser:")
            for ingrediens in extra_ingredienser:
                print(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr")
                total_pris += ingrediens.ingrediens_pris  # Lägg till priset för extra ingredienser till totalpriset
        
        if bästa_match:
            print("Bästa matchningar:")
            for sallad in bästa_match:
                print(sallad.namn_sallad)
        if kompletterande_ingredienser:
            print("Kompletterande ingredienser:")
            for ingrediens in kompletterande_ingredienser:
                print(ingrediens)
        print(f"Totalt pris: {total_pris} kr")

    
    def skriv_kvittot_till_fil(self, filnamn, valda_ingredienser, extra_ingredienser, total_pris, bästa_matchning=None, kompletterande_ingredienser=None):
        """
        Skriver ut ett kvitto med de valda ingredienserna, eventuella extra ingredienser, och det totala priset till en fil.
        """
        with open(filnamn, 'w', encoding='utf-8') as f:
            f.write("Här är ditt kvitto:\n")
            f.write("Valda ingredienser:\n")
            for ingrediens in valda_ingredienser:
                f.write(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr\n")
            if extra_ingredienser:
                f.write("Extra ingredienser:\n")
                for ingrediens in extra_ingredienser:
                    f.write(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr\n")
            if bästa_matchning:
                f.write("Bästa matchning:\n")
                for sallad in bästa_matchning:
                    f.write(f"{sallad.namn_sallad}\n")
            
            if kompletterande_ingredienser:
                f.write("Kompletterande ingredienser:\n")
                for ingrediens in kompletterande_ingredienser:
                    f.write(f"{ingrediens}\n")
            f.write(f"Totalt pris: {total_pris} kr\n")


    def bearbeta_salladval(self):
        """
        Koordinerar de andra funktionerna för att bearbeta användarens salladval.
        """
        self.läs_in_sallader()
        self.läs_in_ingredienser()

        while True:
            print("""
                Välj ett alternativ från menyn nedan:
                (a) Skapa en egen sallad.
                (b) Avsluta programmet.
                """)

            val = input("Alternativ: ")
            if val.lower() == 'a':
                valda_ingredienser = self.välj_ingredienser()
                matchningar, kompletterande_ingredienser, totalpris = self.hitta_matchande_sallader(valda_ingredienser)
                extra_ingredienser = self.välj_extra_ingredienser()
                print("""
                Välj ett alternativ från menyn nedan:
                (a) Skriv ut kvittot till skärmen.
                (b) Skriv ut kvittot till en fil.
                """)
                val = input("Alternativ: ")
                if val.lower() == 'a':
                    self.skriv_kvittot(valda_ingredienser, extra_ingredienser, totalpris, matchningar, kompletterande_ingredienser)
                elif val.lower() == 'b':
                    filnamn = 'kvitto.txt'
                    self.skriv_kvittot_till_fil(filnamn, valda_ingredienser, extra_ingredienser, totalpris, matchningar, kompletterande_ingredienser)
                else:
                    print("Ogiltigt val. Försök igen.")
            elif val.lower() == 'b':
                break
            else:
                print("Ogiltigt val. Försök igen.")


def main():
    """
    Huvudfunktionen som skapar en Salladbar-instans och bearbetar användarens salladval.
    """
    salladbar = Salladbar()
    salladbar.bearbeta_salladval()

if __name__ == "__main__":
    main()