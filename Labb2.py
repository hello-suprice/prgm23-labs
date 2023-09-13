def läs_in_flyttal(prompt):
    while True:
        try:
            värde = float(input(prompt))
            return värde
        except ValueError:
            print("Det där var inte ett flyttal. Försök igen.")

def läs_in_heltal(prompt):
    while True:
        try:
            värde = int(input(prompt))
            return värde
        except ValueError:
            print("Det där var inte ett heltal. Försök igen.")

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
        if val == 1:

            try:
            
                # Användaren matar in värden för aritmetiska summan:
                start_värde_aritmetisk = läs_in_flyttal("Ange det första värdet för den aritmetiska talföljden: \n")
                diffrens = läs_in_flyttal("Ange differensen för den aritmetiska talföljden: \n")
                antalet_element_aritmetisk = läs_in_heltal("Ange antalet elementer för den aritmetiska talföljden: \n")
                
                # Beräkna och skriv ut resultaten för aritmetiska summan
                aritmetisk_resultat = aritmetisk_summa(start_värde_aritmetisk, diffrens, antalet_element_aritmetisk)
                print("Den aritmetiska summan är: ", aritmetisk_resultat, "\n")

            except:
                print("Något gick fel. Försök igen med giltiga värden. \n")
                continue

        elif val == 2:

            try:
            
                # Användaren matar in värden för geometriska summan:
                start_värde_geometrisk = läs_in_flyttal("Ange det första värdet för den geometriska talföljden: \n")
                kvot = läs_in_flyttal("Ange kvoten för den geometriska talföljden: \n")
                antal_element_geometrisk = läs_in_heltal("Ange antalet elementer för den geometriska talföljden: \n")

                # Beräkna och skriv ut resultaten för geometriska summan:
                geometrisk_resultat = geometrisk_summa(start_värde_geometrisk, kvot, antal_element_geometrisk)
                print("Den geometriska summan är: ", geometrisk_resultat)
            
            except:
                print("Något gick fel. Försök igen med giltiga värden. \n")
                continue
        
        elif val == 3:
            try:
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
                    start_värde_aritmetisk1 = float(input("Skriv in startvärdet för det aritmetiska talföljden: "))
                    diffrens1 = float(input("Skriv in differensen: "))
                    antalet_element_aritmetisk1 = int(input("Ange antalet elementer för den aritmetiska talföljden: "))
                    resultat1 = aritmetisk_summa(start_värde_aritmetisk1, diffrens1, antalet_element_aritmetisk1)
                else:
                    start_värde_geometrisk1 = float(input("Skriv in startvärdet för det geometriska talföljden: "))
                    kvot1 = float(input("Skriv in kvoten: "))
                    antal_element_geometrisk1 = int(input("Ange antalet elementer för den geometriska talföljden: "))
                    resultat1 = geometrisk_summa(start_värde_geometrisk1, kvot1, antal_element_geometrisk1)

                # Användaren matar in värden för den andra summan
                summa2 = input("Är den andra summan [a]ritmetisk eller [g]eometrisk? ").lower()
                if summa2 not in ('a', 'g'):
                    print("Ogiltigt val. Var vänlig välj 'a' för aritmetisk eller 'g' för geometrisk.")
                    continue
                
                if summa2 == 'a':
                    start_värde_aritmetisk2 = float(input("Skriv in startvärdet för det aritmetiska talföljden: "))
                    diffrens2 = float(input("Skriv in differensen: "))
                    antalet_element_aritmetisk2 = int(input("Ange antalet elementer för den aritmetiska talföljden: "))
                    resultat2 = aritmetisk_summa(start_värde_aritmetisk2, diffrens2, antalet_element_aritmetisk2)
                else:
                    start_värde_geometrisk2 = float(input("Skriv in startvärdet för det geometriska talföljden: "))
                    kvot2 = float(input("Skriv in kvoten: "))
                    antal_element_geometrisk2 = int(input("Ange antalet elementer för den geometriska talföljden: "))
                    resultat2 = geometrisk_summa(start_värde_geometrisk2, kvot2, antal_element_geometrisk2)

                # Jämför de två summorna
                if resultat1 > resultat2:
                    print("Den första summan är störst. \n")
                elif resultat1 < resultat2:
                    print("Den andra summan är störst. \n")
                else:
                    print("Båda summorna är lika stora. \n")
                
                
            except ValueError:
                print("Felaktig inmatning. Var vänlig mata in numeriska värden igen. \n")
                continue

        else:
            print("Felaktigt val! Välj en siffra mellan 1 och 4. \n")
        
        val = läs_in_heltal("Vad vill du göra? ")
    print("Avslutar \n")
meny()