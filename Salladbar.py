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
        self.ingreidenser = []
    
    def läs_in_sallader(self):
        """
        Läser in sallader från en JSON-fil och lagrar dem i en lista.
        """
        pass
        
    def läs_in_ingredienser(self):
        """
        Läser in ingredienser från en JSON-fil och lagrar dem i en lista.
        """
        pass

    def välj_ingredienser(self):
        """
        Låter användaren välja ingredienser för sin sallad.
        """
        pass


    def hitta_matchande_sallader(self, valda_ingredienser):
        """
        Hittar alla sallader som matchar de valda ingredienserna.
        """
        pass


    def välj_extra_ingredienser(self):
        """
        Låter användaren välja extra ingredienser.
        """
        pass

    def skriv_kvittot(self, vald_sallad, extra_ingredienser):
        """
        Skriver ut ett kvitto till en fil.
        """
        pass

    def bearbeta_salladval(self):
        """
        Koordinerar de andra funktionerna för att bearbeta användarens salladval.
        """
        pass

def main():
    """
    Huvudfunktionen som skapar en Salladbar-instans och bearbetar användarens salladval.
    """
    salladbar = Salladbar()
    salladbar.bearbeta_salladval()

if __name__ == "__main__":
    main()