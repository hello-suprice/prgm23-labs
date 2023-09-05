# Funktion för att beräkna summan av en aritmetisk talföljd
def aritmetisk_summa(a1, d, n):
    '''
    Beräknar summan av en aritmetisk talföljd med det första elementvärdet a_1,
    differensen d mellan elementerna och antalet elementer n, enligt formeln för aritmetisk summa.
    '''
    summa = n * (2 * a1 + (n - 1) * d) / 2 #Formeln för arimetisk summa med aritmetisk följd för sista talet i följden
    return summa

# Funktion för att beräkna summan av en geometrisk talföljd
def geometrisk_summa(g1, q, n):
    '''
    Beräknar summan av en geometrisk talföljd med det första elementvärdet g_1,
    kvoten q mellan elementerna och antalet element n, enligt formeln för geometrisk summa.
    '''
    summa = g1 * (((g1 * q**(n-1)) - 1) / (q - 1)) #Formeln för geometrisk summa med geometrisk följd för sista talet i följden
    return summa

# Användaren matar in värden:
a1 = float(input("Skriv in startvärdet (a1): \n"))
d = float(input("Ange differensen (d) för den aritmetiska talföljden: \n"))
n1 = int(input("Ange antalet elementer (n) för den aritmetiska talföljden: \n"))

# Beräkna och skriv ut resultaten
aritmetisk_resultat = aritmetisk_summa(a1, d, n1)
print("Den aritmetiska summan är: ", aritmetisk_resultat)

# Användaren matar in värden:
g1 = float(input("Ange det första värdet (g_1) för den geometriska talföljden: \n"))
q = float(input("Ange kvoten (q) för den geometriska talföljden: \n"))
n2 = int(input("Ange antalet elementer (n) för den geometriska talföljden: \n"))


# Beräkna och skriv ut resultaten
geometrisk_resultat = geometrisk_summa(g1, q, n2)
print("Den geometriska summan är: ", geometrisk_resultat)

    
  
