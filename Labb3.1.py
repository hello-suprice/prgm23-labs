import typed_input

def aritmetisk_summa(a1, d, n):
    '''
    Beräknar summan av en aritmetisk talföljd med det första elementvärdet a_1,
    differensen d mellan elementerna och antalet elementer n, enligt formeln för aritmetisk summa.
    '''
    summa = n * (2 * a1 + (n - 1) * d) / 2
    return summa

def geometrisk_summa(g1, q, n):
    '''
    Beräknar summan av en geometrisk talföljd med det första elementvärdet g_1,
    kvoten q mellan elementerna och antalet element n, enligt formeln för geometrisk summa.
    '''
    summa = ( g1 * ((q**(n)) - 1) / (q - 1))
    return summa

def läs_in_talföljd():
    '''
    Låter användaren mata in information om en talföljd, inklusive typ, startvärde och relevanta parametrar.

    :return: En tupel med information om talföljden: (talföljd_typ, start_värde, diffrens/kvot).
    '''

    while True:
        talföljd_typ = input("Är talföljden [a]ritmetisk eller [g]eometrisk? ").lower()
        if talföljd_typ not in ('a', 'g'):
            print("Ogiltigt val. Välj 'a' för aritmetisk eller 'g' för geometrisk.")
        else:
            break
    '''
    Koden nedan jämför två talföljder och lagrar talföljdens typ (antingen 'aritmetisk' eller 'geometrisk')
    i variabeln följd. Detta görs för att ge en tydligare beskrivning av vilken typ av talföljd som användaren har valt
    istället för att enbart använda bokstäverna 'a' eller 'g' som identifierare.
    '''
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
    '''
    Låter användaren jämföra två talföljder och visar vilken som är störst eller om de är lika stora.
    '''

    print("Data för den första summan:")
    talföljd_typ1, start_värde1, parameter1 = läs_in_talföljd()
    '''
    Anropar funktionen 'läs_in_talföljd' för att låta användaren mata in information om den första och andra talföljden.
    Resultatet av funktionen lagras i variabler 'talföljd_typ', 'start_värde', och 'parameter'.
    '''
    print("\nData för den andra summan:")
    talföljd_typ2, start_värde2, parameter2 = läs_in_talföljd()
    
    
    antal_element = typed_input.läs_in_heltal("\nSkriv in antalet element i följden: ")
    
    while antal_element <= 0:
        print("Antalet element måste vara större än noll.")
        antal_element = typed_input.läs_in_heltal("Skriv in värdet på antal element igen: ")

    '''
    Koden under jämför två talföljder, antingen aritmetiska eller geometriska, baserat på användarens val.
    Resultaten och typen av talföljder (aritmetiska eller geometriska) sparas i variabler för slutet av koden.
    '''
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

    '''
    Koden under jämför resultatet av två talföljder 
    och skriver ut vilken typ av talföljd som är störst,
    eller om de är lika stora.
    '''
    if resultat1 > resultat2:
        print(f"Den {talföljd_typ1} summan är störst.")
    elif resultat1 < resultat2:
        print(f"Den {talföljd_typ2} summan är störst.")
    else:
        print("Båda summorna är lika stora.")

def meny():
    
    '''
    Huvudmeny för programmet som låter användaren välja mellan olika alternativ
    för att beräkna aritmetiska och geometriska summor samt jämföra två summor.
    '''
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
        '''
        Så länge valet är skilt från 4 det vill säga avsluta programmet 
        så kommer koden gå igenom resten av koden, beroende vilken val man väljer.
        '''
        if val == 1:
            '''
            Val 1 kommer räkna ut aritmetiska summan
            '''
            # Användaren matar in värden för aritmetiska summan:
            start_värde_aritmetisk = typed_input.läs_in_flyttal("Ange det första värdet för den aritmetiska talföljden: ")
            diffrens = typed_input.läs_in_flyttal("Ange differensen för den aritmetiska talföljden: ")
            
            antalet_element_aritmetisk = typed_input.läs_in_heltal("Ange antalet elementer för den aritmetiska talföljden: ")
            '''
            En while-loop som kontrollerar om antalet element är mindre än eller lika med noll.
            Om det är fallet, betyder det att användaren har angett ett ogiltigt värde för antalet element,
            och en felmeddelande skrivs ut för att informera användaren om att antalet element måste vara större än noll.
            '''
            while antalet_element_aritmetisk <= 0:
                print("Antalet element måste vara större än noll.")
                '''
                Ett meddelande skrivs ut som informerar användaren om att antalet element måste vara större än noll.
                Därefter uppmanas användaren att skriva in värdet på antalet element igen med hjälp av 
                `typed_input.läs_in_heltal`-funktionen. Loopen fortsätter att köra tills användaren anger ett giltigt värde
                för antalet element, det vill säga ett heltal större än noll.
                '''
                antalet_element_aritmetisk = typed_input.läs_in_heltal("Skriv in värdet på antalet element igen: ")

            # Beräknar och skriver ut resultaten för aritmetiska summan
            aritmetisk_resultat = aritmetisk_summa(start_värde_aritmetisk, diffrens, antalet_element_aritmetisk)
            print("Den aritmetiska summan är: ", aritmetisk_resultat, "\n")



        elif val == 2:
            '''
            Val 2 kommer räkna ut geometriska summan.
            '''
            # Användaren matar in värden för geometriska summan:
            start_värde_geometrisk = typed_input.läs_in_flyttal("Ange det första värdet för den geometriska talföljden: ")
            
            kvot = typed_input.läs_in_flyttal("Ange kvoten för den geometriska talföljden: ")
            '''
            Loopen ser till att förhindra nolldivision genom att inte tillåta q att vara ekvivalent med 1.
            '''
            while kvot == 0 or kvot == 1:
                print("Kvoten kan inte vara 0 eller 1. Försök igen.")
                kvot = typed_input.läs_in_flyttal("Skriv in värdet på kvoten igen: ")

            
            antal_element_geometrisk = typed_input.läs_in_heltal("Ange antalet elementer för den geometriska talföljden: ")
            
            while antal_element_geometrisk <= 0:
                print("Antal element måste vara större än noll.")
                antal_element_geometrisk = typed_input.läs_in_heltal("Skriv in värdet på antalet element igen: ")
            

            # Beräknar och skriver ut resultaten för geometriska summan:
            geometrisk_resultat = geometrisk_summa(start_värde_geometrisk, kvot, antal_element_geometrisk)
            print("Den geometriska summan är: ", geometrisk_resultat, "\n")
        
    
        elif val == 3:
           jämför_summor()
        
        else:
            print("Felaktigt val! Välj en siffra mellan 1 och 4. \n") 
            '''
            Om användaren inte väljer ett alternativ mellan 1-4 kommer ett felmeddelande att skrivas ut
            där programet kommer poängtera att du måste välja mellan 1-4.
            '''
        
        val = typed_input.läs_in_heltal("Vad vill du göra? ")
    print("Avslutar \n")
meny()
