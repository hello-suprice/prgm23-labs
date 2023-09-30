class Student:
    """
    En klass för att representera en student.
    """
    def __init__(self, fornamn, efternamn, personnummer):
        """
        Konstruktorn för klassen Student.
        """
        self.fornamn = fornamn
        self.efternamn = efternamn
        self.personnummer = personnummer

    def __str__(self):
        """
        Returnerar en strängrepresentation av studentobjektet.
        """
        return f"Namn: {self.fornamn} {self.efternamn} Personnr: {self.personnummer}"

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
    fornamn = input("Förnamn: ")
    efternamn = input("Efternamn: ")
    personnummer = hämta_giltigt_personnummer()
    student = Student(fornamn, efternamn, personnummer)
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

def uppdatera_student():
    personnummer_to_update = input("Skriv in personnumret på objektet du vill ändra: ")
    for student in studenter:
        if student.personnummer == personnummer_to_update:
            choice = input(print(f"Vill du ändra namn på {student.first_name} {student.last_name} (Ja eller nej)? "))
            if choice.lower() == 'ja':
                new_first_name = input("Skriv in det nya förnamnet: ")
                new_last_name = input("Skriv in det nya efternamnet: ")
                student.first_name = new_first_name
                student.last_name = new_last_name
                print(f"Nu är namnet för {student.personnummer} ändrat till {new_first_name} {new_last_name}!")
                break
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
        uppdatera_student()
    elif val.lower() == 'q':
        break
    else:
        print("Ogiltigt val. Försök igen.")

print("Här är alla sparade objekt:")
for student in studenter:
    print(student)
