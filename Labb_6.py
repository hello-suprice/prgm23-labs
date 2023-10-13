'''
Skapad av Teeshk N, Henrik A & Simon B
Kom åt koden här: https://codeshare.io/PdrnmQ
'''
import os

class Person:
    def __init__(self, förnamn, efternamn, personnummer):
        '''
        Konstruktorn för klassen persson.
        '''
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer
    
    def __str__(self):
        return f"{self.förnamn} {self.efternamn}, {self.personnummer}"



class Student(Person):
    def __init__(self, förnamn, efternamn, personnummer, roll):
        super().__init__(förnamn, efternamn, personnummer)
        self.roll = roll
    def __str__(self):
        return f"Namn: {self.förnamn} {self.efternamn} Personnr: {self.personnummer} Roll: {self.roll}"


class School:
    '''
    En klass för att representera en skola.
    '''
    
    def __init__(self):
        self.studenter = []
        self.filnamn = None

    def läs_in_från_fil(self):
        '''
        Läser in studenter från en fil. Funktionen frågar användaren 
        om filnamnet om det inte redan har angetts. Sedan läser den in 
        varje rad från filen, skapar en ny Student för varje rad och lägger 
        till dem i listan self.studenter.
        '''
        if self.filnamn is None:
            self.filnamn = input("Vad heter filen med alla studenter? ")
            while not os.path.exists(self.filnamn):
                print("Den filen fanns inte! Skriv in en ny fil: ")
                self.filnamn = input()

        with open(self.filnamn, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(0, len(lines), 3):
                personnummer = lines[i].strip()
                efternamn = lines[i+1].strip()
                förnamn = lines[i+2].strip()
                roll = 'student'
                self.studenter.append(Student(förnamn, efternamn, personnummer, roll))
    
    def spara_till_fil(self, student):
        '''
        Sparar en given student till filen. Funktionen öppnar filen i 'append'-läge och lägger till den nya studenten i slutet av filen.
    
        Args:
            student (Student): Studentobjektet som ska sparas till filen.
        '''
        if self.filnamn is not None:
            print(f"Sparar student till fil: {student}")
            with open(self.filnamn, 'a') as f:
                f.write(f"{student.personnummer}\n{student.efternamn}\n{student.förnamn}\n")

    
    def skriv_till_fil(self):
        '''
        Skriver om listan av studenter till filen. Funktionen öppnar filen i 
        'write'-läge och skriver om hela filen med den aktuella listan över studenter.
        '''
        with open(self.filnamn, 'w', encoding='utf-8') as f:
            for student in self.studenter:
                f.write(f"{student.personnummer}\n{student.efternamn}\n{student.förnamn}\n")

    def hämta_giltigt_personnummer(self):
        '''
        Funktion för att få ett korrekt skriver personnummer som inte används.
        '''
        while True:
            personnummer = input("Personnummer: ")
            personummer_använt = False
            for lista in [self.studenter]:
                for person in lista:
                    if personnummer == person.personnummer:
                        personummer_använt = True
                        break
            if personnummer.isdigit() and len(personnummer) == 10 and not personummer_använt:
                return personnummer
            else:
                print("Personnumret får bara innehålla 10 siffror och inte vara i användning, försök igen!")

    
    def lägg_till_person(self):
        '''
        Funktion för att lägga till en ny student.
        '''
        while True:
            print("Lägg till en ny student:")
            förnamn = input("Förnamn: ")
            efternamn = input("Efternamn: ")
            if förnamn.isalpha() and efternamn.isalpha():
                personnummer = self.hämta_giltigt_personnummer()
                break
            else:
                print("Välj ett namn som endast inehåller bokstäver, försök igen!")
        
        student = Student(förnamn, efternamn, personnummer, 'student')
        
        
        print(f"Lägger till student: {student}")


        self.spara_till_fil(student)
                
        print("""
        Personen tillagd!
        """)

    
    def visa_alla_personer(self):
        self.studenter = []
        self.läs_in_från_fil()

        print("Här är alla studenter på KTH:")
        for student in self.studenter:
            print(student)

    
    def lägg_till_personer(self):
        '''
        Funktion för att lägga till flera personer.
        '''
        antal_personer = läs_in_heltal("Hur många personer vill du lägga till? ")
        for _ in range(antal_personer):
            self.lägg_till_person()

    
    def ta_bort_person(self):
        '''
        Funktion för att ta bort en befintlig person.
        '''
        personnummer_att_ta_bort = input("Skriv in personnumret på objektet du vill ta bort: ")
        for lista in [self.studenter]:
            for person in lista:
                if person.personnummer == personnummer_att_ta_bort:
                    lista.remove(person)
                    print(f"Objektet med personnummer {personnummer_att_ta_bort} har tagits bort!")
                    self.skriv_till_fil() #Skriv om listan till filen
                    return
        print("Inget objekt med det personnumret hittades.")

    
    def ändra_person(self):
        '''
        Funktion för att ändra en befintlig person.
        '''
        personnummer_ändra = input("Skriv in personnumret på personen du vill ändra: ")
        for lista in [self.studenter]:
            for person in lista:
                if person.personnummer == personnummer_ändra:
                    val = input(f"Vill du ändra namn på {person.förnamn} {person.efternamn} (ja eller nej)?: ")
                    if val.lower() == 'ja':
                        person.förnamn = input("Skriv in det nya förnamnet: ")
                        person.efternamn = input("Skriv in det nya efternamnet: ")
                        print(f"Nu är namnet för {person.personnummer} ändrat till {person.förnamn} {person.efternamn}!")
                        self.skriv_till_fil()
                    else:
                        print("Inget ändrades.")
                    return
        print("Inget objekt med det personnumret hittades.")

    
    def sök_efter_person(self):
        '''
        Funktion för att söka efter en person.
        '''
        if not self.studenter:
            print("Det finns inga personer att söka efter ännu.")
            return
        while True:
            sökt_person = input("Vad heter personen du söker efter?: ")
            for lista in [self.studenter]:
                for person in lista:
                    if person.förnamn + " " + person.efternamn == sökt_person:
                        print(f"Namn: {person.förnamn} {person.efternamn} \nPersonnr: {person.personnummer} \nRoll: {person.roll}")
                        return
            print("Personen du sökte efter finns inte, försök igen")
            

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
    '''
    Huvudfunktionen som kör tills användaren väljer att avsluta programmet.
    Användaren presenteras med en meny med alternativ för att lägga till, 
    ta bort, ändra eller söka efter personer i skolan.
    Efter varje operation visas alla sparade objekt.
    '''
    skola = School()
    skola.läs_in_från_fil()
    while True:
        print("""
            Välj ett alternativ från menyn nedan:
            (l) Lägg till en ny person.
            (m) Lägg till flera nya personer.
            (t) Ta bort en befintlig person.
            (a) Ändra en befintligt person.
            (s) Sök efter en person            
            (q) Avsluta programmet
            """)

        val = input("Alternativ: ")
        if val.lower() == 'l':
            skola.lägg_till_person()
            skola.visa_alla_personer()
        elif val.lower() == 'm':
            skola.lägg_till_personer()
            skola.visa_alla_personer()
        elif val.lower() == 't':
            skola.ta_bort_person()
        elif val.lower() == 'a':
            skola.ändra_person()
        elif val.lower() == 's':
            skola.sök_efter_person()
        elif val.lower() == 'q':
            break
        else:
            print("Ogiltigt val. Försök igen.")

    print("Här är alla sparade objekt:\n")
    print("Här är alla studenter på KTH:")
    for student in skola.studenter:
        print(student)

main()
