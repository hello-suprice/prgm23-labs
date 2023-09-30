class Student:
    def __init__(self, first_name, last_name, personnummer):
        self.first_name = first_name
        self.last_name = last_name
        self.personnummer = personnummer

    def __str__(self):
        return f"Namn: {self.first_name} {self.last_name} Personnr: {self.personnummer}"

def get_valid_personnummer():
    while True:
        personnummer = input("Vad är studentens personnummer? ")
        if personnummer.isdigit() and len(personnummer) == 10:
            return personnummer
        else:
            print("Personnumret får bara innehålla 10 siffror, försök igen!")

def add_student():
    print("Lägg till en ny student:")
    first_name = input("Förnamn: ")
    last_name = input("Efternamn: ")
    personnummer = get_valid_personnummer()
    student = Student(first_name, last_name, personnummer)
    students.append(student)
    print("Objektet skapat!\n")

def add_students():
    antal_studenter = int(input("Hur många studenter vill du lägga till? "))
    for _ in range(antal_studenter):
        add_student()

def remove_student():
    personnummer_to_remove = input("Skriv in personnumret på objektet du vill ta bort: ")
    for student in students:
        if student.personnummer == personnummer_to_remove:
            students.remove(student)
            print(f"Objektet med personnummer {personnummer_to_remove} har tagits bort!")
            break
    else:
        print("Inget objekt med det personnumret hittades.")

students = []

while True:
    print("Vill du lägga till (l) en student, lägga till (m) flera studenter, ta bort (t) en student eller avsluta (q)?")
    choice = input()
    if choice.lower() == 'l':
        add_student()
    elif choice.lower() == 'm':
        add_students()
    elif choice.lower() == 't':
        remove_student()
    elif choice.lower() == 'q':
        break
    else:
        print("Ogiltigt val. Försök igen.")

print("Här är alla sparade objekt:")
for student in students:
    print(student)
