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
    
class School:
    """
    En klass för att representera en skola.
    """
    def __init__(self):
        self.studenter = []

    @staticmethod
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

    def lägg_till_student(self):
        """
        Funktion för att lägga till en ny student.
        """
        print("Lägg till en ny student:")
        förnamn = input("Förnamn: ")
        efternamn = input("Efternamn: ")
        personnummer = self.hämta_giltigt_personnummer()
        student = Student(förnamn, efternamn, personnummer)
        self.studenter.append(student)
        print("Objektet skapat!\n")

    def lägg_till_studenter(self):
        """
        Funktion för att lägga till flera studenter.
        """
        antal_studenter = int(input("Hur många studenter vill du lägga till? "))
        for _ in range(antal_studenter):
            self.lägg_till_student()

def main(): 
    skola = School()
    while True:
        print("""
            Välj ett alternativ från menyn nedan:
            (l) Lägg till en ny student
            (m) Lägg till flera nya studenter
            (q) Avsluta programmet
            """)

        val = input()
        if val.lower() == 'l':
            skola.lägg_till_student()
        elif val.lower() == 'm':
            skola.lägg_till_studenter()
        elif val.lower() == 'q':
            break
        else:
            print("Ogiltigt val. Försök igen.")

main()
