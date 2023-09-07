def aritmetisk_summa(a1, d, n):
    '''
    Beräknar summan av en aritmetisk talföljd med det första elementvärdet a_1,
    differensen d mellan elementerna och antalet elementer n, enligt formeln för aritmetisk summa.
    '''
    summa = n * (2 * a1 + (n - 1) * d) / 2 #Formeln för arimetisk summa med aritmetisk följd för sista elementet i följden
    return summa

def geometrisk_summa(g1, q, n):
    '''
    Beräknar summan av en geometrisk talföljd med det första elementvärdet g_1,
    kvoten q mellan elementerna och antalet element n, enligt formeln för geometrisk summa.
    '''
    summa = ( g1 * ((q**(n)) - 1) / (q - 1)) #Formeln för geometrisk summa med geometrisk följd för sista elementet i följden
    return summa

# Användaren matar in värden:
start_värde_aritmetisk = float(input("Ange det första värdet för den geometriska talföljden: \n"))
diffrens = float(input("Ange differensen för den aritmetiska talföljden: \n"))
antalet_element_aritmetisk = int(input("Ange antalet elementer för den aritmetiska talföljden: \n"))

# Beräkna och skriv ut resultaten
aritmetisk_resultat = aritmetisk_summa(start_värde_aritmetisk, diffrens, antalet_element_aritmetisk)
print("Den aritmetiska summan är: ", aritmetisk_resultat)

# Användaren matar in värden:
start_värde_geometrisk = float(input("Ange det första värdet för den geometriska talföljden: \n"))
kvot = float(input("Ange kvoten för den geometriska talföljden: \n"))
antal_element_geometrisk = int(input("Ange antalet elementer för den geometriska talföljden: \n"))


# Beräkna och skriv ut resultaten
geometrisk_resultat = geometrisk_summa(start_värde_geometrisk, kvot, antal_element_geometrisk)
print("Den geometriska summan är: ", geometrisk_resultat)

    
  
