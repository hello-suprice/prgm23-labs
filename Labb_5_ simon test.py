'''
Skapad av Teeshk N, Henrik A & Simon B
Kom åt koden här: https://codeshare.io/vwvDnK
'''

class Person:
    def __init__(self, förnamn, efternamn, personnummer):
        """
        Konstruktorn för klassen persson.
        """
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer
    
    def __str__(self):
        return f"{self.förnamn} {self.efternamn}, {self.personnummer}"

class Lärare(Person):
    def __init__(self, förnamn, efternamn, personnummer, roll):
        super().__init__(förnamn, efternamn, personnummer)
        self.roll = roll
    def __str__(self):
        return f"Namn: {self.förnamn} {self.efternamn} Personnr: {self.personnummer} Roll: {self.roll}"

class Student(Person):
    def __init__(self, förnamn, efternamn, personnummer, roll):
        super().__init__(förnamn, efternamn, personnummer)
        self.roll = roll
    def __str__(self):
        return f"Namn: {self.förnamn} {self.efternamn} Personnr: {self.personnummer}  Roll: {self.roll}"

class School:
    """
    En klass för att representera en skola.
    """
    
    def __init__(self):
        self.studenter = []
        self.lärare = []
    @staticmethod
    def hämta_giltigt_personnummer():
        """
        Funktion för att få ett giltigt personnummer från användaren.
        """
        while True:
            personnummer = input("Vad är studentens personnummer? ")
            if personnummer.isdigit() and len(personnummer) == 2:
                return personnummer
            else:
                print("Personnumret får bara innehålla 2 siffror, försök igen!")
    
    def lägg_till_student(self):
        """
        Funktion för att lägga till en ny student.
        """
        
        print("Lägg till en ny student:")
        förnamn = input("Förnamn: ")
        efternamn = input("Efternamn: ")
        personnummer = self.hämta_giltigt_personnummer()
        
        while True:
            lärare_eller_student = input("Är det en [l]ärare eller [s]tudent")    
            if lärare_eller_student == "s":
                roll = "student"
                student = Student(förnamn, efternamn, personnummer, roll)
                self.studenter.append(student)
                break
            elif lärare_eller_student == "l":
                roll = "lärare"
                student = Lärare(förnamn, efternamn, personnummer, roll)
                self.lärare.append(student)
                break
            else:
                print("Något gick fel försök igen")
                
        
        print("""
        Personen tillagd!
        """)

    def visa_alla_personer(self):
        print("Här är alla studenter på KTH:")
        for student in self.studenter:
            print(student)
        
        print("\nHär är alla lärare på KTH:")
        for lärare in self.lärare:
            print(lärare)
    
    def lägg_till_studenter(self):
        """
        Funktion för att lägga till flera studenter.
        """
        antal_studenter = läs_in_heltal("Hur många studenter vill du lägga till? ")
        for _ in range(antal_studenter):
            self.lägg_till_student()
    
    def ta_bort_student(self):
        """
        Funktion för att ta bort en befintlig student.
        """
        personnummer_att_ta_bort = input("Skriv in personnumret på objektet du vill ta bort: ")
        for student in self.studenter:
            if student.personnummer == personnummer_att_ta_bort:
                self.studenter.remove(student)
                print(f"Objektet med personnummer {personnummer_att_ta_bort} har tagits bort!")
                break
        else:
            print("Inget objekt med det personnumret hittades.")
    
    def ändra_student(self):
        '''
        Funktion för att ändra en befintligt student
        '''
        personnummer_ändra = läs_in_heltal("Skriv in personnumret på studenten du vill ändra: ")
        for student in self.personer:
            if student.personnummer == personnummer_ändra:
                print(f"Vill du ändra namn på {student.förnamn} {student.efternamn} (Ja eller nej)? ")
                val = input()
                if val.lower() == 'ja':
                    student.förnamn = input("Skriv in det nya förnamnet: ")
                    student.efternamn = input("Skriv in det nya efternamnet: ")
                    print(f"Nu är namnet för {student.personnummer} ändrat till {student.förnamn} {student.efternamn}!")
                else:
                    print("Inget ändrades.")
                break
        else:
            print("Inget objekt med det personnumret hittades.")


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


def main(): 
    skola = School()
    while True:
        print("""
            Välj ett alternativ från menyn nedan:
            (l) Lägg till en ny person.
            (m) Lägg till flera nya personer.
            (t) Ta bort en befintlig person.
            (a) Ändra en befintligt person.
            (q) Avsluta programmet
            """)

        val = input()
        if val.lower() == 'l':
            skola.lägg_till_student()
            skola.visa_alla_personer()
        elif val.lower() == 'm':
            skola.lägg_till_studenter()
            skola.visa_alla_personer()
        elif val.lower() == 't':
            skola.ta_bort_student()
        elif val.lower() == 'a':
            skola.ändra_student()
        elif val.lower() == 'q':
            break
        else:
            print("Ogiltigt val. Försök igen.")

    print("Här är alla sparade objekt:\n")
    print("Här är alla studenter på KTH:")
    for student in skola.studenter:
        print(student)
    print("\nHär är alla studenter på KTH:")
    for lärare in skola.lärare:
        print(lärare)
main()
