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
            return värde #Funktionen returnerar det inmatade flyttalet som en flyttalsvariabel (float). 
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
            return värde #Funktionen returnerar det inmatade heltalet som en heltalsvariabel (int). 
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
                        Välkommen till Sum Meny. Välj ett av alternativen nedan:
                1. Räkna ut aritmetisk summa.                     2. Räkna ut geometrisk summa.
                                         
                                             3. Jämför två summor
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
                
            # Beräkna och skriv ut resultaten för aritmetiska summan
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

            # Beräkna och skriv ut resultaten för geometriska summan:
            geometrisk_resultat = geometrisk_summa(start_värde_geometrisk, kvot, antal_element_geometrisk)
            print("Den geometriska summan är: ", geometrisk_resultat)
        
    
        elif val == 3:
            '''
            Val 3 kommer att jämför 2 olika summor,
            antingen artimetisk och geometrisk eller två av samma. 
            '''
            
            # Användaren matar in värden för den första summan
            summa1 = input("Är den första summan [a]ritmetisk eller [g]eometrisk? ").lower()
            if summa1 not in ('a', 'g'):
                print("Ogiltigt val. Var vänlig välj 'a' för aritmetisk eller 'g' för geometrisk.")
                continue
            '''
            Felhantering för användarinput om den första summan i menyval 3.
            Om användaren inte anger 'a' eller 'g', oavsett om det är med stora bokstäver. 
            Kommer det visa ett felmeddelande och låta loopen fortsätta sin exekvering.
            '''
            
            if summa1 == 'a':
                start_värde_aritmetisk1 = läs_in_flyttal("Skriv in startvärdet för det aritmetiska talföljden: ")
                diffrens1 = läs_in_flyttal("Skriv in differensen: ")
                antalet_element_aritmetisk1 = läs_in_heltal("Ange antalet elementer för den aritmetiska talföljden: ")
                resultat1 = aritmetisk_summa(start_värde_aritmetisk1, diffrens1, antalet_element_aritmetisk1)
            else:
                start_värde_geometrisk1 = läs_in_flyttal("Skriv in startvärdet för det geometriska talföljden: ")
                kvot1 = läs_in_flyttal("Skriv in kvoten: ")
                antal_element_geometrisk1 = läs_in_heltal("Ange antalet elementer för den geometriska talföljden: ")
                resultat1 = geometrisk_summa(start_värde_geometrisk1, kvot1, antal_element_geometrisk1)

            # Användaren matar in värden för den andra summan
            summa2 = input("Är den andra summan [a]ritmetisk eller [g]eometrisk? ").lower()
            if summa2 not in ('a', 'g'):
                print("Ogiltigt val. Var vänlig välj 'a' för aritmetisk eller 'g' för geometrisk.")
                continue
            
            if summa2 == 'a':
                start_värde_aritmetisk2 = läs_in_flyttal("Skriv in startvärdet för det aritmetiska talföljden: ")
                diffrens2 = läs_in_flyttal("Skriv in differensen: ")
                antalet_element_aritmetisk2 = läs_in_heltal("Ange antalet elementer för den aritmetiska talföljden: ")
                resultat2 = aritmetisk_summa(start_värde_aritmetisk2, diffrens2, antalet_element_aritmetisk2)
            else:
                start_värde_geometrisk2 = läs_in_flyttal("Skriv in startvärdet för det geometriska talföljden: ")
                kvot2 = läs_in_flyttal("Skriv in kvoten: ")
                antal_element_geometrisk2 = läs_in_heltal("Ange antalet elementer för den geometriska talföljden: ")
                resultat2 = geometrisk_summa(start_värde_geometrisk2, kvot2, antal_element_geometrisk2)

            # Jämför de två summorna
            if resultat1 > resultat2:
                print("Den första summan är störst. \n")
            elif resultat1 < resultat2:
                print("Den andra summan är störst. \n")
            else:
                print("Båda summorna är lika stora. \n")
                
                

        else:
            print("Felaktigt val! Välj en siffra mellan 1 och 4. \n")
        
        val = läs_in_heltal("Vad vill du göra? ")
    print("Avslutar \n")
meny()