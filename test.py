import typed_input

def aritmetisk_summa(a1, d, n):
    return n * (2 * a1 + (n - 1) * d) / 2

def geometrisk_summa(g1, q, n):
    if q == 1:
        raise ValueError("Kvoten kan inte vara 1 för en geometrisk summa.")
    return g1 * ((q**n) - 1) / (q - 1)

def läs_in_talföljd():
   
    while True:
        talföljd_typ = input("Är talföljden [a]ritmetisk eller [g]eometrisk? ").lower()
        if talföljd_typ not in ('a', 'g'):
            print("Ogiltigt val. Välj 'a' för aritmetisk eller 'g' för geometrisk.")
        else:
            break
    
    if talföljd_typ == 'a':
        följd = 'aritmetisk'
    else:
        följd = 'geometrisk'
    start_värde = typed_input.läs_in_flyttal(f"Skriv in startvärdet för den {följd} talföljden: ")
    
    if talföljd_typ == 'a':
        diffrens = typed_input.läs_in_flyttal("Skriv in differensen: ")
        
    else:
        kvot = typed_input.läs_in_flyttal("Skriv in kvoten: ")
        while kvot == 0 or kvot == 1:
            print("Kvoten kan inte vara 0 eller 1 för en geometrisk talföljd.")
            kvot = typed_input.läs_in_flyttal("Skriv in värdet på kvoten igen: ")
    
    
    return talföljd_typ, start_värde, diffrens if talföljd_typ == 'a' else kvot

def jämför_summor():
    print("Data för den första summan:")
    talföljd_typ1, start_värde1, parameter1 = läs_in_talföljd()
    

    print("\nData för den andra summan:")
    talföljd_typ2, start_värde2, parameter2 = läs_in_talföljd()
    
    
    antal_element = typed_input.läs_in_heltal("\nSkriv in antalet element i följden: ")
    
    while antal_element <= 0:
        print("Antalet element måste vara större än noll.")
        antal_element = typed_input.läs_in_heltal("Skriv in värdet på antal element igen: ")

    
    if talföljd_typ1 == 'a':
        resultat1 = aritmetisk_summa(start_värde1, parameter1, antal_element)
        talföljd_typ1 = 'aritmetiska'
    else:
        resultat1 = geometrisk_summa(start_värde1, parameter1, antal_element)
        talföljd_typ1 = 'geometriska'
    if talföljd_typ2 == 'a':
        resultat2 = aritmetisk_summa(start_värde2, parameter2, antal_element)
        talföljd_typ2 = 'aritmetiska'
    else:
        resultat2 = geometrisk_summa(start_värde2, parameter2, antal_element)
        talföljd_typ2 = 'geometriska'

    if resultat1 > resultat2:
        print(f"Den {talföljd_typ1} summan är störst.")
    elif resultat1 < resultat2:
        print(f"Den {talföljd_typ2} summan är störst.")
    else:
        print("Båda summorna är lika stora.")

def meny():
    print(
        """
        --- Meny ---
        Välkommen till Summa Meny. Välj ett av alternativen nedan:
        1. Räkna ut aritmetisk summa.
        2. Räkna ut geometrisk summa.
        3. Jämför två summor.
        4. Avsluta.
        """
    )

    val = typed_input.läs_in_heltal("Vad vill du göra? ")

    while val != 4:
        if val == 1:
            start_värde_aritmetisk = typed_input.läs_in_flyttal("Ange det första värdet för den aritmetiska talföljden: ")
            diffrens = typed_input.läs_in_flyttal("Ange differensen för den aritmetiska talföljden: ")
            antalet_element_aritmetisk = typed_input.läs_in_heltal("Ange antalet elementer för den aritmetiska talföljden: ")
            
            while antalet_element_aritmetisk <= 0:
                print("Antalet element måste vara större än noll.")
                antalet_element_aritmetisk = typed_input.läs_in_heltal("Skriv in värdet på antalet element igen: ")

            aritmetisk_resultat = aritmetisk_summa(start_värde_aritmetisk, diffrens, antalet_element_aritmetisk)
            print("Den aritmetiska summan är:", aritmetisk_resultat)
        
        elif val == 2:
            start_värde_geometrisk = typed_input.läs_in_flyttal("Ange det första värdet för den geometriska talföljden: ")
            kvot = typed_input.läs_in_flyttal("Ange kvoten för den geometriska talföljden: ")
            
            while kvot == 0 or kvot == 1:
                print("Kvoten kan inte vara 0 eller 1. Försök igen.")
                kvot = typed_input.läs_in_flyttal("Skriv in värdet på kvoten igen: ")
            
            antal_element_geometrisk = typed_input.läs_in_heltal("Ange antalet elementer för den geometriska talföljden: ")
            
            while antal_element_geometrisk <= 0:
                print("Antalet element måste vara större än noll.")
                antal_element_geometrisk = typed_input.läs_in_heltal("Skriv in värdet på antalet element igen: ")

            geometrisk_resultat = geometrisk_summa(start_värde_geometrisk, kvot, antal_element_geometrisk)
            print("Den geometriska summan är:", geometrisk_resultat)
        
        elif val == 3:
            jämför_summor()
        
        else:
            print("Felaktigt val! Välj en siffra mellan 1 och 4.")

        val = typed_input.läs_in_heltal("Vad vill du göra? ")

    print("Avslutar")

meny()
