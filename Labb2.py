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


    print("Meny:\n1.Räkna ut aritmetisk summa\n2.Räkna ut geometriskt summa.\n3.Jämför två summor. \n4.Avsluta")
    val = int(input("Vad vill du göra?"))
    while val != 4:
        if val == 1:

            try:
            
                # Användaren matar in värden för aritmetiska summan:
                start_värde_aritmetisk = float(input("Ange det första värdet för den aritmetiska talföljden: \n"))
                diffrens = float(input("Ange differensen för den aritmetiska talföljden: \n"))
                antalet_element_aritmetisk = int(input("Ange antalet elementer för den aritmetiska talföljden: \n"))
                
                # Beräkna och skriv ut resultaten för aritmetiska summan
                aritmetisk_resultat = aritmetisk_summa(start_värde_aritmetisk, diffrens, antalet_element_aritmetisk)
                print("Den aritmetiska summan är: ", aritmetisk_resultat)

            except:
                print("Något gick fel. Försök igen med giltiga värden. \n")
                continue

        elif val == 2:

            try:
            
                # Användaren matar in värden för geometriska summan:
                start_värde_geometrisk = float(input("Ange det första värdet för den geometriska talföljden: \n"))
                kvot = float(input("Ange kvoten för den geometriska talföljden: \n"))
                antal_element_geometrisk = int(input("Ange antalet elementer för den geometriska talföljden: \n"))

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
                Om användaren inte anger 'a' eller 'g', oavsett om det är med stora bokstäver 
                eftersom jag använder mig av lower() som omvandlar det till litenbokstav. 
                Vilket visas ett felmeddelande och loopen fortsätter.
                '''
                
                if summa1 == 'a':
                    start_värde_aritmetisk1 = float(input("Skriv in startvärdet (a1): "))
                    diffrens1 = float(input("Skriv in differensen (d): "))
                    antalet_element_aritmetisk1 = int(input("Hur många termer (n)? "))
                    resultat1 = aritmetisk_summa(start_värde_aritmetisk1, diffrens1, antalet_element_aritmetisk1)
                else:
                    start_värde_geometrisk1 = float(input("Skriv in startvärdet (g1): "))
                    kvot1 = float(input("Skriv in kvoten (q): "))
                    antal_element_geometrisk1 = int(input("Hur många termer (n)? "))
                    resultat1 = geometrisk_summa(start_värde_geometrisk1, kvot1, antal_element_geometrisk1)

                # Användaren matar in värden för den andra summan
                summa2 = input("Är den andra summan [a]ritmetisk eller [g]eometrisk? ").lower()
                if summa2 not in ('a', 'g'):
                    print("Ogiltigt val. Var vänlig välj 'a' för aritmetisk eller 'g' för geometrisk.")
                    continue
                
                if summa2 == 'a':
                    start_värde_aritmetisk2 = float(input("Skriv in startvärdet (a1): "))
                    diffrens2 = float(input("Skriv in differensen (d): "))
                    antalet_element_aritmetisk2 = int(input("Hur många termer (n)? \n"))
                    resultat2 = aritmetisk_summa(start_värde_aritmetisk2, diffrens2, antalet_element_aritmetisk2)
                else:
                    start_värde_geometrisk2 = float(input("Skriv in startvärdet (g1): "))
                    kvot2 = float(input("Skriv in kvoten (q): "))
                    antal_element_geometrisk2 = int(input("Hur många termer (n)? \n"))
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

        else:
            print("Felaktigt val! Välj en siffra mellan 1 och 4. \n")
        
        val = int(input("Vad vill du göra? \n"))
    print("Avslutar")
meny()