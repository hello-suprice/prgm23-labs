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

def main():
    print("Data för den aritmetiska summan:")
    a1 = typed_input.läs_in_flyttal("Skriv in värdet på a1: ")
    d = typed_input.läs_in_flyttal("Skriv in värdet på d: ")
   
    print("Data för den geometrisk summan:")
    g1 = typed_input.läs_in_flyttal("Skriv in värdet på g1: ")
    q = typed_input.läs_in_flyttal("Skriv in värdet på q: ")

    while q == 1:
        q = typed_input.läs_in_heltal("Skriv in värdet på kovten igen, kan ej vara 1. Vi får nolldivision: ")
  
    print("Antal termer i summorna:")
    n = typed_input.läs_in_heltal("Skriv in värdet på n: ")
    while n <= 0:
        n = typed_input.läs_in_heltal("Antal element(n) måste vara större än noll. \nSkriv in värdet på n: ")
        break
    
    aritmetisk = aritmetisk_summa(a1, d, n)
    geometrisk = geometrisk_summa(g1, q, n)
  
    if aritmetisk > geometrisk:
        print(f"Den aritmetiska summan är störst. \n")
    elif aritmetisk < geometrisk:
        print(f"Den geometriska summan är störst. \n")
    else:
        print("Båda summorna är lika stora. \n")

main()