'''
Skapad av Teeshk N, Henrik A & Simon B
Kom åt koden här: https://codeshare.io/vwvDnK
'''

class Student:
    """
    En klass för att representera en student.
    """
    def __init__(self, förnamn, efternamn, personnummer):
        """
        Konstruktorn för klassen Student.
        """
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer

    def __str__(self):
        """
        Returnerar en strängrepresentation av studentobjektet.
        """
        return f"Namn: {self.förnamn} {self.efternamn} Personnr: {self.personnummer}"

def hämta_giltigt_personnummer():
    """
    Funktion för att få ett giltigt personnummer från användaren.
    """
    while True:
        personnummer = input("Vad är studentens personnummer? ")
        if personnummer.isdigit() and len(personnummer) == 10:
            return personnummer
        else:
            print("Personnumret får bara innehålla 10 siffror, försök igen!")

def lägg_till_student():
    """
    Funktion för att lägga till en ny student.
    """
    print("Lägg till en ny student:")
    förnamn = input("Förnamn: ")
    efternamn = input("Efternamn: ")
    personnummer = hämta_giltigt_personnummer()
    student = Student(förnamn, efternamn, personnummer)
    studenter.append(student)
    print("Objektet skapat!\n")

def lägg_till_studenter():
    """
    Funktion för att lägga till flera studenter.
    """
    antal_studenter = int(input("Hur många studenter vill du lägga till? "))
    for _ in range(antal_studenter):
        lägg_till_student()

def ta_bort_student():
    """
    Funktion för att ta bort en befintlig student.
    """
    personnummer_att_ta_bort = input("Skriv in personnumret på objektet du vill ta bort: ")
    for student in studenter:
        if student.personnummer == personnummer_att_ta_bort:
            studenter.remove(student)
            print(f"Objektet med personnummer {personnummer_att_ta_bort} har tagits bort!")
            break
    else:
        print("Inget objekt med det personnumret hittades.")

def ändra_student():
    '''
    Funktion för att ändra en befintligt student
    '''
    personnummer_ändra = input("Skriv in personnumret på studenten du vill ändra: ")
    for student in studenter:
        if student.personnummer == personnummer_ändra:
            print(f"Vill du ändra namn på {student.förnamn} {student.efternamn} (Ja eller nej)? ")
            choice = input()
            if choice.lower() == 'ja':
                student.förnamn = input("Skriv in det nya förnamnet: ")
                student.efternamn = input("Skriv in det nya efternamnet: ")
                print(f"Nu är namnet för {student.personnummer} ändrat till {student.förnamn} {student.efternamn}!")
            else:
                print("Inget ändrades.")
            break
    else:
        print("Inget objekt med det personnumret hittades.")


studenter = []

while True:
    print("""
          Välj ett alternativ från menyn nedan:
          (l) Lägg till en ny student
          (m) Lägg till flera nya studenter
          (t) Ta bort en befintlig student
          (a) Ändra en befintligt student
          (q) Avsluta programmet
          """)

    val = input()
    if val.lower() == 'l':
        lägg_till_student()
    elif val.lower() == 'm':
        lägg_till_studenter()
    elif val.lower() == 't':
        ta_bort_student()
    elif val.lower() == 'a':
        ändra_student()
    elif val.lower() == 'q':
        break
    else:
        print("Ogiltigt val. Försök igen.")

print("Här är alla sparade objekt:")
for student in studenter:
    print(student)
