'''
Kopiera denna länk för att komma åt koden än från kth grejen, det blir lättare:
https://codeshare.io/Qn3KwR
'''


def läs_in_flyttal(prompt):
    '''
    Läser in ett flyttal från användaren med angivet prompt.
    '''
    while True:
        try:
            värde = float(input(prompt)) 
            '''
            En sträng som innehåller meddelandet som visas för användaren för att instruera dem att mata in ett flyttal.
            '''
            return värde 
        except ValueError:
            print("Det där var inte ett flyttal. Försök igen.")
            '''
            Om användaren matar in något som inte kan tolkas som ett giltigt flyttal, 
            kommer funktionen att kasta ett ValueError och skriva ut ett felmeddelande.
            '''

def läs_in_heltal(prompt):
    '''
    Läser in ett heltal från användaren med angivet prompt.
    '''
    while True:
        try:
            värde = int(input(prompt)) 
            '''
            En sträng som innehåller meddelandet som visas för användaren för att instruera dem att mata in ett heltal.
            '''
            return värde 
        except ValueError:
            print("Det där var inte ett heltal. Försök igen.") 
            '''
            Om användaren matar in något som inte kan tolkas som ett giltigt heltal, 
            kommer funktionen att kasta ett ValueError och skriva ut ett felmeddelande.
            '''

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



def meny():
    
    '''
    Huvudmeny för programmet som låter användaren välja mellan olika alternativ
    för att beräkna aritmetiska och geometriska summor samt jämföra två summor.
    '''
    print(
            """
                                             --- Meny ---
                        Välkommen till Summa Meny. Välj ett av alternativen nedan:
                1. Räkna ut aritmetisk summa.                     2. Räkna ut geometrisk summa.
                                         
                3. Jämför två summor                              4. Avsluta.
            ---------------------------------------------------------------------------------------
            """)

    val = läs_in_heltal("Vad vill du göra? ")
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
            start_värde_aritmetisk = läs_in_flyttal("Ange det första värdet för den aritmetiska talföljden: \n")
            diffrens = läs_in_flyttal("Ange differensen för den aritmetiska talföljden: \n")
            antalet_element_aritmetisk = läs_in_heltal("Ange antalet elementer för den aritmetiska talföljden: \n")
                
            # Beräknar och skriver ut resultaten för aritmetiska summan
            aritmetisk_resultat = aritmetisk_summa(start_värde_aritmetisk, diffrens, antalet_element_aritmetisk)
            print("Den aritmetiska summan är: ", aritmetisk_resultat, "\n")



        elif val == 2:
            '''
            Val 2 kommer räkna ut geometriska summan.
            '''
            # Användaren matar in värden för geometriska summan:
            start_värde_geometrisk = läs_in_flyttal("Ange det första värdet för den geometriska talföljden: \n")
            kvot = läs_in_flyttal("Ange kvoten för den geometriska talföljden: \n")
            antal_element_geometrisk = läs_in_heltal("Ange antalet elementer för den geometriska talföljden: \n")

            # Beräknar och skriver ut resultaten för geometriska summan:
            geometrisk_resultat = geometrisk_summa(start_värde_geometrisk, kvot, antal_element_geometrisk)
            print("Den geometriska summan är: ", geometrisk_resultat)
        
    
        elif val == 3:
            '''
            Val 3 kommer att jämför 2 olika summor,
            antingen artimetisk och geometrisk eller två av samma. 
            '''
            
            summa1 = input("Är den första summan [a]ritmetisk eller [g]eometrisk? ").lower()
            if summa1 not in ('a', 'g'):
                print("Ogiltigt val. Var vänlig välj 'a' för aritmetisk eller 'g' för geometrisk.")
                continue
            '''
            Felhantering för användarinput om den första summan i menyval 3.
            Om användaren inte anger 'a' eller 'g', oavsett om det är med stora bokstäver. 
            Kommer det visa ett felmeddelande och låta loopen fortsätta sin exekvering.
            '''

            
            '''
            Koden under används för att samla in användarens input för två olika talföljder, antingen aritmetiska eller geometriska, baserat på användarens val.
            Det skrivs också ut en beskrivning av talföljden som användaren valt.
            '''
            if summa1 == 'a':
                print("Data för den aritmetiska summan:")
                start_värde_aritmetisk1 = läs_in_flyttal("Skriv in startvärdet för det aritmetiska talföljden: ")
                diffrens1 = läs_in_flyttal("Skriv in differensen: ")
                print("")
                
            else:
                print("Data för den geometriska summan:")
                start_värde_geometrisk1 = läs_in_flyttal("Skriv in startvärdet för det geometriska talföljden: ")
                kvot1 = läs_in_flyttal("Skriv in kvoten: ")
                print("")

            
            summa2 = input("Är den andra summan [a]ritmetisk eller [g]eometrisk? ").lower()
            if summa2 not in ('a', 'g'):
                print("Ogiltigt val. Var vänlig välj 'a' för aritmetisk eller 'g' för geometrisk.")
                continue
            
            if summa2 == 'a':
                print("Data för den aritmetiska summan:")
                start_värde_aritmetisk2 = läs_in_flyttal("Skriv in startvärdet för det aritmetiska talföljden: ")
                diffrens2 = läs_in_flyttal("Skriv in differensen: ")
                print("")
                
            else:
                print("Data för den geometriska summan:")
                start_värde_geometrisk2 = läs_in_flyttal("Skriv in startvärdet för det geometriska talföljden: ")
                kvot2 = läs_in_flyttal("Skriv in kvoten: ")
                print("")
                
            
            antalet_element = läs_in_heltal("Skriv in antalet element i följden för båda :")


            '''
    	    Koden under jämför två talföljder, antingen aritmetiska eller geometriska, baserat på användarens val.
            Resultaten och typen av talföljder (aritmetiska eller geometriska) sparas i variabler för slutet av koden.
            '''
            if summa1 == 'a':
                resultat1 = aritmetisk_summa(start_värde_aritmetisk1, diffrens1, antalet_element)
                summa1 = 'aritmetiska'
            else:
                resultat1 = geometrisk_summa(start_värde_geometrisk1, kvot1, antalet_element)
                summa1 = 'geometriska'
            if summa2 == 'a':
                resultat2 = aritmetisk_summa(start_värde_aritmetisk2, diffrens2, antalet_element)
                summa2 = 'aritmetiska'
            else:
                resultat2 = geometrisk_summa(start_värde_geometrisk2, kvot2, antalet_element)
                summa2 = 'geometriska'
    

            '''
            Koden under jämför resultatet av två talföljder 
            och skriver ut vilken typ av talföljd som är störst,
            eller om de är lika stora.
            '''
            if resultat1 > resultat2:
                print(f"Den {summa1} summan är störst. \n")
            elif resultat1 < resultat2:
                print(f"Den {summa2} summan är störst. \n")
            else:
                print("Båda summorna är lika stora. \n")
                
                
        
        else:
            print("Felaktigt val! Välj en siffra mellan 1 och 4. \n") 
            '''
            Om användaren inte väljer ett alternativ mellan 1-4 kommer ett felmeddelande att skrivas ut
            där programet kommer poängtera att du måste välja mellan 1-4.
            '''
        
        val = läs_in_heltal("Vad vill du göra? ")
    print("Avslutar \n")
meny()
