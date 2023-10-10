
#Labb 5, Grupp 26, Jacob Ivarsson, Elly Isaksson, Theodor Karlsson
"""Programet kan lagra och hatera lärare, studenter och deras personnummer"""
import test2 as fH
class Person:
    """Person innehåller förnamn, efternamn, personnummer samt typ (0 för student
    1 för lärare). Den har metoder för init, str samt en metod för att byta namn
    på personen."""
    def __init__(self, fornamn, efternamn, pNr, typ):
        self.fornamn = fornamn
        self.efternamn = efternamn
        self.pNr = pNr
        self.typ = typ
    
    def __str__(self):
        return f"Namn: {self.fornamn} {self.efternamn}, Personnummer: {self.pNr}"
    
    def bytNamn (self, fornamn, efternamn):
        """Metoden tar in förnamn och efternamn på personen och ändrar de."""
        self.fornamn = fornamn
        self.efternamn = efternamn
class Student(Person):
    """Klassen student ärver allt av klassen person."""
class Larare(Person):
    """Klassen larare ärver allt av klassen person."""
class Skola:
    """Skola är en klass med attributen två listor med elever och lärare. Den har
    init, str samt en metoder."""
    
    def __init__(self):
        self.studenter = []
        self.larare = []
    
    def __str__(self):
        retStr = "\nLärare:\n"
        for lararen in self.larare:
            retStr += f"{lararen}\n"
        retStr += "\nStudenter:\n"
        for student in self.studenter:
            retStr += f"{student}\n"
        return retStr


def skapaPerson (studenter, larare, antal):
    """Metoden är en metod för att skapa nya personer och lägga till de i listan.
    Den tar in
    en referens till listan och antal personer som ska läggas till. Den returnerar
    list-referensen och uppdaterar huvudlistan."""
    i = 0
    for i in range(antal):
        typ = fH.felHanteringTyp()
        namnL = fH.felhanteringNamn()
        fNamn = namnL[0]
        eNamn = namnL[1]
        for namnet in namnL:
            if (namnL[0] not in namnet) and (namnL[1] not in namnet):
                eNamn = f"{eNamn} {namnet}"
        pNr = fH.felhanteringPnr(input("Vad har personen för personnummer? "))
        if typ == 0:
            nyStudent = Student(fNamn, eNamn, pNr, typ)
            studenter.append(nyStudent)
        elif typ == 1:
            nyLarare= Larare(fNamn, eNamn, pNr, typ)
            larare.append(nyLarare)
        print("Person skapad!")
        i += 1
    return studenter, larare
def andraPerson(pNr, studenter, larare):
    """Metoden ändrar namnet på en person med hjälp av ändraNamn metoden i
    person klassen. Den tar in personnummret på personen som skall ändras
    och en referens till listan. Uppdaterar listan och skickar tillbaka
    en referens som uppdaterar huvudlistan."""
    personHittad = False
    for student in studenter:
        if pNr == student.pNr:
            namnL = fH.felhanteringNamn()
            fNamn = namnL[0]
            eNamn = namnL[1]
            for namnet in namnL:
                if (namnL[0] not in namnet) and (namnL[1] not in namnet):
                    eNamn = f"{eNamn} {namnet}"
            student.bytNamn(fNamn, eNamn)
            print(student)
            personHittad = True
    for lararen in larare:
        if pNr == lararen.pNr:
            namnL = fH.felhanteringNamn()
            fNamn = namnL[0]
            eNamn = namnL[1]
            for namnet in namnL:
                if (namnL[0] not in namnet) and (namnL[1] not in namnet):
                    eNamn = f"{eNamn} {namnet}"
            lararen.bytNamn(fNamn, eNamn)
            print(lararen)
            personHittad = True
    if not personHittad:
        print("Personnumret finns inte i någon lista!")
    return studenter, larare

def taBortPerson(pNr, studenter, larare):
    """Metoden tar bort en student med hjälp av listan och ett personnummer. Tar in
    referens till listan och ett personnummer på vem som ska bort. Därefter
    returnerar den en uppdaterad referens till listan."""
    personHittad = False
    for student in studenter:
        if pNr == student.pNr:
            studenter.remove(student)
            print(f"{student} borttagen!")
            personHittad = True
    for lararen in larare:
        if pNr == lararen.pNr:
            studenter.remove(lararen)
            print(f"{lararen} borttagen!")
            personHittad = True
    if not personHittad:
        print("Personnumret finns inte i någon lista!")
    return studenter, larare

def printSkolan(skolan):
    """Skriver ut alla personer med hjälp av en referens till skolan."""
    print(skolan)

def huvudprogram ():
    """Programmets huvuddel"""
    kor = True
    skolan = Skola()
    print("Börja med att mata in en person!")
    skolan.studenter, skolan.larare = skapaPerson(skolan.studenter, skolan.larare, 1)
    while kor:
        try:
            val = int(input("\n === Meny === \n(1) Lägga till person\n(2) Ändra person\n(3) Ta bort person\n(4) Skriva ut alla personer\n(5) Avsluta programmet\nVal: "))
            if val == 1:
                inmatTest = True
                while inmatTest:
                    try:
                        antal = abs(int(input("Hur många personer vill du lägga till? ")))
                        inmatTest = False
                    except ValueError:
                            print("Felaktig inmatning! Det måste vara ett heltal!")
                print("")
                skolan.studenter, skolan.larare = skapaPerson(skolan.studenter, skolan.larare, antal)
            elif val == 2:
                pNr = fH.felhanteringPnr(input("Vad har personen för personnummer?"))
                skolan.studenter, skolan.larare = andraPerson(pNr, skolan.studenter, skolan.larare)
            elif val == 3:
                pNr = fH.felhanteringPnr(input("Vad har personen för personnummer?"))
                skolan.studenter, skolan.larare = taBortPerson(pNr, skolan.studenter, skolan.larare)
            elif val == 4:
                printSkolan(skolan)
            elif val == 5:
                quit()
            else:
                print("Vänligen välj alternativen 1-5")
        except ValueError:
            print("Det där var inte ett godkänt val!")
huvudprogram()
