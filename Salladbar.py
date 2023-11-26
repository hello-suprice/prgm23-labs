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
        
        for i, ingrediens in enumerate(self.ingredienser, start=1):   # https://www.geeksforgeeks.org/enumerate-in-python/
            print(f"{i}. {ingrediens}")
        print("Välj dina ingredienser:")
        while True:
            kontroll_nummer = input().split(',')
            valda_nummer = set(kontroll_nummer)
            if len(kontroll_nummer) != len(valda_nummer):
                print("Ogiltigt val. Du har valt samma nummer flera gånger")
                continue
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
        
        # Kontrollera om de valda ingredienserna finns i alla sallader
        """
        if all(set(valda_ingredienser_namn).issubset(set(sallad.ingredienser)) for sallad in self.sallader):
            print("Du har valt ingredienser som finns i alla sallader. Det finns ingen bästa matchande sallad.")
            total_pris = sum(ingrediens.ingrediens_pris for ingrediens in valda_ingredienser)
            print(f"Totalkostnaden blir {total_pris} kr.")
            return self.sallader, None, total_pris
        """
       
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
                    bästa_match_pris = sallad.sallad_pris
                    bästa_match_kompletterande_ingredienser = kompletterande_ingredienser

            if not kompletterande_ingredienser:
                print(f"Bästa matchande sallad är {bästa_match.namn_sallad} med priset {bästa_match.sallad_pris} kr.")
                print("Du behöver inte lägga till några kompletterande ingredienser eftersom du redan har alla ingredienser i denna sallad.")
                valda_ingredienser_pris = sum(ingrediens.ingrediens_pris for ingrediens in valda_ingredienser if ingrediens.namn_ingrediens not in bästa_match.ingredienser)
                bästa_match_pris += valda_ingredienser_pris
                print(f"Totalkostnaden blir {bästa_match_pris} kr.")
                return [bästa_match], None, bästa_match_pris

            print(f"Bästa matchande sallad är {bästa_match.namn_sallad} med priset {bästa_match.sallad_pris} kr.")
            print(f"Du kan lägga till dessa ingredienser: {', '.join(bästa_match_kompletterande_ingredienser)}")

            while True:
                svar = input("Vill du lägga till de kompletterande ingredienserna? (ja/nej) ")
                if svar.lower() == 'ja':
                    valda_ingredienser_pris = sum(ingrediens.ingrediens_pris for ingrediens in valda_ingredienser if ingrediens.namn_ingrediens not in bästa_match.ingredienser)
                    bästa_match_pris += valda_ingredienser_pris
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
        
        print("Välj ingredienser att lägga till genom att ange deras nummer, separerade med kommatecken, eller skriv 'klar' när du är färdig: ")
        extra_ingredienser = []  # Definiera extra_ingredienser som en tom lista före loopen
        while True:

            val = input()
            
            if val.lower() == 'klar':
                break
            
            valda_nummer = val.split(',')
            unika_nummer = set(valda_nummer)
            if len(valda_nummer) != len(unika_nummer):
                print("Ogiltigt val. Du har valt samma nummer.")
                continue
            try: 
                for nummer in valda_nummer:
                    if not nummer.isdigit() or not 1 <= int(nummer) <= len(self.ingredienser):
                        raise ValueError
                extra_ingredienser = [ingrediens for i, ingrediens in enumerate(self.ingredienser, start=1) if str(i) in valda_nummer]
                break
            except ValueError:
                print(f"""
                      Ogiltigt inmatning {nummer}. Ange numren för dina valda ingredienser, 
                      separerade med kommatecken eller skriv 'klar' om du inte vill ha extra ingredienser.
                      """)
        
        
        return extra_ingredienser

    def skriv_kvittot(self, valda_ingredienser, extra_ingredienser, total_pris, bästa_match=None, kompletterande_ingredienser=None):
        """
        Skriver ut ett kvitto med de valda ingredienserna, eventuella extra ingredienser, och det totala priset.
        """
        print("""
              HÄR ÄR DITT KVITTO: \n
              """)
        print("Valda ingredienser:")
        for ingrediens in valda_ingredienser:
            print(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr")
    
        if extra_ingredienser:
            print("Extra ingredienser:")
            for ingrediens in extra_ingredienser:
                print(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr")
                total_pris += ingrediens.ingrediens_pris  # Lägg till priset för extra ingredienser till totalpriset
        
        if bästa_match:
            print("\nBästa matchningar:")
            for sallad in bästa_match:
                print(sallad.namn_sallad)
        if kompletterande_ingredienser:
            print("\nKompletterande ingredienser:")
            for ingrediens in kompletterande_ingredienser:
                print(ingrediens)
        print(f"\nTotalt pris: {total_pris} kr")

    
    def skriv_kvittot_till_fil(self, filnamn, valda_ingredienser, extra_ingredienser, total_pris, bästa_matchning=None, kompletterande_ingredienser=None):
        """
        Skriver ut ett kvitto med de valda ingredienserna, eventuella extra ingredienser, och det totala priset till en fil.
        """
        with open(filnamn, 'w', encoding='utf-8') as f:
            f.write("""
                    HÄR ÄR DITT KVITTO:
                    """)
            f.write("\nValda ingredienser:\n")
            for ingrediens in valda_ingredienser:
                f.write(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr\n")
            if extra_ingredienser:
                f.write("\nExtra ingredienser:\n")
                for ingrediens in extra_ingredienser:
                    f.write(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr\n")
                    total_pris += ingrediens.ingrediens_pris
            if bästa_matchning:
                f.write("\nBästa matchning:\n")
                for sallad in bästa_matchning:
                    f.write(f"{sallad.namn_sallad}\n")
            
            if kompletterande_ingredienser:
                f.write("\nKompletterande ingredienser:\n")
                for ingrediens in kompletterande_ingredienser:
                    f.write(f"{ingrediens}\n")
            f.write(f"\nTotalt pris: {total_pris} kr\n")


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
                
                self.skriv_kvittot(valda_ingredienser, extra_ingredienser, totalpris, matchningar, kompletterande_ingredienser)
                filnamn = 'kvitto.txt'
                self.skriv_kvittot_till_fil(filnamn, valda_ingredienser, extra_ingredienser, totalpris, matchningar, kompletterande_ingredienser)
                
                
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