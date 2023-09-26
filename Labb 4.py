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

def update_student():
    personnummer_to_update = input("Skriv in personnumret på objektet du vill ändra: ")
    for student in students:
        if student.personnummer == personnummer_to_update:
            choice = input(print(f"Vill du ändra namn på {student.first_name} {student.last_name} (Ja eller nej)?"))
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
    print("Vill du lägga till (l), ändra (a), ta bort (t) ett objekt eller avsluta (q)?")
    choice = input()
    if choice.lower() == 'l':
        add_student()
    elif choice.lower() == 'a':
        update_student()
    elif choice.lower() == 't':
        remove_student()
    elif choice.lower() == 'q':
        break
    else:
        print("Ogiltigt val. Försök igen.")

print("Här är alla sparade objekt:")
for student in students:
    print(student)
