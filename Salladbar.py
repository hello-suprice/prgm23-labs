import json 
import sys

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
    
    def läs_in_sallader(self, filnamn_sallader):
        """
        Läser in sallader från en JSON-fil och lagrar dem i en lista.
        """
        try:
            with open(filnamn_sallader, 'r', encoding='utf-8') as f:
                sallader_data = json.load(f)
                for sallad_data in sallader_data:
                    namn_sallad = sallad_data["namn_sallad"]
                    sallad_pris = sallad_data["sallad_pris"]
                    ingredienser = sallad_data["ingredienser"]
                    self.sallader.append(Sallad(namn_sallad, sallad_pris, ingredienser))
        except FileNotFoundError:
            print("Kunde inte hitta filen json filen för sallader. Kontrollera att filen finns och försök igen.")
            sys.exit(1)  # Avsluta programmet med felkoden 1
        
    def läs_in_ingredienser(self, filnamn_ingredienser):
        """
        Läser in ingredienser från en JSON-fil och lagrar dem i en lista.
        """
        try:
            with open(filnamn_ingredienser, 'r', encoding='utf-8') as f:
                ingredienser_data = json.load(f)
                for ingrediens_data in ingredienser_data:
                    namn_ingrediens = ingrediens_data["namn_ingrediens"]
                    ingreidens_pris = ingrediens_data["ingrediens_pris"]
                    self.ingredienser.append(Ingrediens(namn_ingrediens, ingreidens_pris))
        except FileNotFoundError:
            print("Kunde inte hitta json filen för ingredienser. Kontrollera att filen finns och försök igen.")
            sys.exit(1)  # Avsluta programmet med felkoden 1

    def rens_listor(self):
        """
        Rensar listorna för sallader och ingredienser.
        """
        self.sallader.clear()
        self.ingredienser.clear()

    def välj_ingredienser(self):
        """
        Låter användaren välja ingredienser för sin sallad.
        """
        
        # Skriver ut en numerisk lista av tillgängliga ingredienser
        for i, ingrediens in enumerate(self.ingredienser, start=1):   # https://www.geeksforgeeks.org/enumerate-in-python/
            print(f"{i}. {ingrediens}")
        print("Välj dina ingredienser:")
        
        # Loopar tills användaren ger en giltig inmatning
        while True:

            # Läser in användarens inmatning och separerar den med kommatecken
            kontroll_nummer = input().split(',')
            valda_nummer = set(kontroll_nummer)
            
            # Kollar om användaren valt samma ingrediens flera gånger
            if len(kontroll_nummer) != len(valda_nummer):
                print("Ogiltigt val. Du har valt samma nummer flera gånger")
                continue
            try: 
                # Kontrollerar om användarens val är giltiga nummer och ligger inom gränserna av tillgängliga ingredienser
                for nummer in valda_nummer:
                    if not nummer.isdigit() or not 1 <= int(nummer) <= len(self.ingredienser):
                        raise ValueError
                break
            except ValueError:
                # Om valen är ogiltiga, meddelar användaren och ber att göra om valet
                print("Ogiltigt inmatning. Ange numren för dina valda ingredienser, separerade med kommatecken.")
        
        # Skapar en lista av valda ingredienser baserat på användarens inmatning
        valda_ingredienser = [ingrediens for i, ingrediens in enumerate(self.ingredienser, start=1) if str(i) in valda_nummer]
        
        return valda_ingredienser # Returnerar listan med användarens valda ingredienser


    def hitta_matchande_sallader(self, valda_ingredienser):
        """
        Hittar alla sallader som matchar de valda ingredienserna.
        """
        # Skapar en lista med namnen på de valda ingredienserna
        valda_ingredienser_namn = [ingrediens.namn_ingrediens for ingrediens in valda_ingredienser]

        # Letar efter perfekta matchningar där ingredienserna exakt matchar salladens ingredienser
        perfekta_matchningar = [sallad for sallad in self.sallader if set(valda_ingredienser_namn) == set(sallad.ingredienser)]
        
        # Om det finns perfekta matchningar
        if perfekta_matchningar:
            # Skriver ut perfekta matchande sallader och beräknar totalpriset för den första matchningen
            print("\nHär är salladen som exakt matchar din valda ingredienser:")
            for sallad in perfekta_matchningar:
                print(sallad)
            total_pris = perfekta_matchningar[0].sallad_pris  # Priset för den perfekta matchningen
            return perfekta_matchningar, None, total_pris

        # Om det inte finns perfekta matchningar
        else:
            # Initialiserar variabler för att spåra bästa matchande salladen
            bästa_match = None
            bästa_match_antal = 0
            bästa_match_pris = float('inf')   
            bästa_match_kompletterande_ingredienser = None

            # Loopar genom alla sallader för att hitta den bästa matchningen
            for sallad in self.sallader:
                matchande_ingredienser = set(valda_ingredienser_namn).intersection(set(sallad.ingredienser))
                kompletterande_ingredienser = set(sallad.ingredienser) - set(valda_ingredienser_namn)
                
                # Uppdaterar variabler om en bättre matchande sallad hittas
                if len(matchande_ingredienser) > bästa_match_antal or (len(matchande_ingredienser) == bästa_match_antal and sallad.sallad_pris  < bästa_match_pris):
                    bästa_match = sallad
                    bästa_match_antal = len(matchande_ingredienser)
                    bästa_match_pris = sallad.sallad_pris
                    bästa_match_kompletterande_ingredienser = kompletterande_ingredienser
            
            # Beräknar priset för de valda ingredienserna som inte redan finns i den bästa matchande salladen
            valda_ingredienser_pris = sum(ingrediens.ingrediens_pris for ingrediens in valda_ingredienser if ingrediens.namn_ingrediens not in bästa_match.ingredienser)

            # Om det inte finns några kompletterande ingredienser att lägga till
            if not bästa_match_kompletterande_ingredienser:
                print(f"\nBästa matchande sallad är {bästa_match.namn_sallad} med priset {bästa_match.sallad_pris} kr.")
                print("Du behöver inte lägga till några kompletterande ingredienser eftersom du redan har alla ingredienser i denna sallad.")
                
                bästa_match_pris += valda_ingredienser_pris
                print(f"Totalkostnaden blir {bästa_match_pris} kr.\n")
                return [bästa_match], None, bästa_match_pris
            
            # Om det finns kompletterande ingredienser att lägga till
            print(f"Bästa matchande sallad är {bästa_match.namn_sallad} med priset {bästa_match.sallad_pris} kr.")
            print(f"Du kan lägga till dessa ingredienser: {', '.join(bästa_match_kompletterande_ingredienser)}")

            # Användarinteraktion för att lägga till kompletterande ingredienser
            while True:
                svar = input("Vill du lägga till de kompletterande ingredienserna? (ja/nej) ")
                if svar.lower() == 'ja':
                    bästa_match_pris += valda_ingredienser_pris
                    print(f"Totalkostnaden blir {bästa_match_pris} kr.\n")
                    return [bästa_match], bästa_match_kompletterande_ingredienser, bästa_match_pris
                elif svar.lower() == 'nej':
                    bara_valda_ingredienser_pris = sum(ingrediens.ingrediens_pris for ingrediens in valda_ingredienser)
                    print(f"Totalkostnaden blir {bara_valda_ingredienser_pris} kr.\n")
                    return [bästa_match], None, bara_valda_ingredienser_pris
                else:
                    print("Skriv ett lämpligt svar ja eller nej!")


    def välj_extra_ingredienser(self):
        """
        Låter användaren välja extra ingredienser.
        """
        print("\nHär är alla tillgängliga extra ingredienser och deras priser:")
        
        # Visar tillgängliga extra ingredienser och deras priser
        for i, ingrediens in enumerate(self.ingredienser, start=1):
            print(f"{i}. {ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr")
        
        # Användarinteraktion för att välja extra ingredienser
        print("""
              Välj extra ingredienser att lägga till genom att ange deras nummer, 
              separerade med kommatecken, eller skriv 'klar' om du inte vill ha 
              extra ingredienser: 
              """)
        extra_ingredienser = []  # Definiera extra_ingredienser som en tom lista före loopen
        while True:

            val = input()
            
            if val.lower() == 'klar':
                break
            
            valda_nummer = val.split(',')
            unika_nummer = set(valda_nummer)
            
            # Kontrollerar om samma nummer valts flera gånger
            if len(valda_nummer) != len(unika_nummer):
                print("Ogiltigt val. Du har valt samma nummer.")
                continue

            try: 
                for nummer in valda_nummer:
                    # Kontrollerar om det valda numret är en siffra och inom rätt intervall
                    if not nummer.isdigit() or not 1 <= int(nummer) <= len(self.ingredienser):
                        raise ValueError
                # Läggs de valda extra ingredienserna till i listan baserat på valda nummer
                extra_ingredienser = [ingrediens for i, ingrediens in enumerate(self.ingredienser, start=1) if str(i) in valda_nummer]
                break
            except ValueError:
                print(f"""
                      Ogiltigt inmatning {nummer}. Ange numren för dina valda ingredienser, 
                      separerade med kommatecken eller skriv 'klar' om du inte vill ha extra ingredienser.
                      """)
        
        
        return extra_ingredienser

    def skriv_kvittot(self, valda_ingredienser, extra_ingredienser, total_pris, bästa_match, kompletterande_ingredienser=None):
        """
        Skriver ut ett kvitto med de valda ingredienserna, eventuella extra ingredienser, och det totala priset.
        """
        # Skriv ut rubrik
        print("""
              HÄR ÄR DITT KVITTO: \n
              """)
        
        # Skriv ut valda ingredienser och deras priser
        print("Valda ingredienser:")
        for ingrediens in valda_ingredienser:
            print(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr")
            
        # Om extra ingredienser har valts, skriv ut dem och lägg till deras priser till totalpriset
        if extra_ingredienser:
            print("\nExtra ingredienser:")
            for ingrediens in extra_ingredienser:
                print(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr")
                total_pris += ingrediens.ingrediens_pris  # Lägg till priset för extra ingredienser till totalpriset
        
        # Skriv ut den bästa matchningen av sallad och dess pris
        print("\nBästa matchning:")
        for sallad in bästa_match:
            print(f"{sallad.namn_sallad}: {sallad.sallad_pris} kr")

        # Om kompletterande ingredienser finns, skriv ut dem
        if kompletterande_ingredienser:
            print("\nKompletterande ingredienser:")
            for ingrediens in kompletterande_ingredienser:
                print(ingrediens)
        
        # Skriv ut det totala priset för hela beställningen
        print(f"\nTotalt pris: {total_pris} kr")

    
    def skriv_kvittot_till_fil(self, filnamn, valda_ingredienser, extra_ingredienser, total_pris, bästa_matchning, kompletterande_ingredienser=None):
        """
        Skriver ut ett kvitto med de valda ingredienserna, eventuella extra ingredienser, och det totala priset till en fil.
        """
        with open(filnamn, 'w', encoding='utf-8') as f:
            f.write("""
                    HÄR ÄR DITT KVITTO:
                    """)
            
            # Skriv ut valda ingredienser och deras priser till filen
            f.write("\nValda ingredienser:\n")
            for ingrediens in valda_ingredienser:
                f.write(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr\n")

            # Om extra ingredienser har valts, skriv ut dem och lägg till deras priser till totalpriset
            if extra_ingredienser:
                f.write("\nExtra ingredienser:\n")
                for ingrediens in extra_ingredienser:
                    f.write(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr\n")
                    total_pris += ingrediens.ingrediens_pris
            
            # Skriv ut den bästa matchningen av sallad till filen
            f.write("\nBästa matchning:\n")
            for sallad in bästa_matchning:
                f.write(f"{sallad.namn_sallad}\n")
            
            # Om kompletterande ingredienser finns, skriv ut dem till filen
            if kompletterande_ingredienser:
                f.write("\nKompletterande ingredienser:\n")
                for ingrediens in kompletterande_ingredienser:
                    f.write(f"{ingrediens}\n")
            
            # Skriv ut det totala priset för hela beställningen till filen
            f.write(f"\nTotalt pris: {total_pris} kr\n")

    def visa_huvudmeny(self):
        """
        Visar huvudmenyn och låter användaren välja vilken salladsbar de vill besöka.
        """
        print("Välkommen! Välj vilken salladsbar du vill besöka:")
        print("1. Kalle på hörnet")
        print("2. Citysallad")
        # Lägga till fler alternativ här om man har fler salladsbarer

        while True:
            val = input()
            if val == '1':
                return 'sallader_KallePåHörnet.json', 'ingredienser_KallePåHörnet.json'
            elif val == '2':
                return 'sallader_Citysallad.json', 'ingredienser_Citysallad.json'
            # Lägga till fler elif-satser om man har fler salladsbarer
            else:
                print("Ogiltigt val. Försök igen.")

    def bearbeta_salladval(self):
        """
        Koordinerar de andra funktionerna för att bearbeta användarens salladval.
        """
        
        
        while True:
            print("""
                Välj ett alternativ från menyn nedan:
                (a) Skapa en egen sallad.
                (b) Byta salladbar.
                (c) Avsluta programmet
                """)

            val = input("Alternativ: ")
            if val.lower() == 'a':
                valda_ingredienser = self.välj_ingredienser() # Användaren väljer ingredienser
                matchningar, kompletterande_ingredienser, totalpris = self.hitta_matchande_sallader(valda_ingredienser) # Matcher valda ingredienser med tillgängliga sallader
                extra_ingredienser = self.välj_extra_ingredienser()
                
                # Skriver ut kvittot för användarens val av sallad och sparar informationen i en fil
                self.skriv_kvittot(valda_ingredienser, extra_ingredienser, totalpris, matchningar, kompletterande_ingredienser)
                filnamn = 'kvitto.txt'
                self.skriv_kvittot_till_fil(filnamn, valda_ingredienser, extra_ingredienser, totalpris, matchningar, kompletterande_ingredienser)
                
                
            elif val.lower() == 'b':
                self.rens_listor()
                filnamn_sallader, filnamn_ingredienser = self.visa_huvudmeny()
                self.läs_in_sallader(filnamn_sallader)
                self.läs_in_ingredienser(filnamn_ingredienser)

            elif val.lower() == 'c':
                break
            else:
                print("Ogiltigt val. Försök igen.")


def main():
    """
    Huvudfunktionen som skapar en Salladbar-instans och bearbetar användarens salladval.
    """
    salladbar = Salladbar()
    filnamn_sallader, filnamn_ingredienser = salladbar.visa_huvudmeny()
    salladbar.läs_in_sallader(filnamn_sallader)
    salladbar.läs_in_ingredienser(filnamn_ingredienser)
    salladbar.bearbeta_salladval()

if __name__ == "__main__":
    main()
