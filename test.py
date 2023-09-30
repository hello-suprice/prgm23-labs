
# Eugenia Pallares, Evangeline Hövenmark, Tua Jacobsson
# 27.09.23
# DD1310 HT23
# Laboration 4: Klasser och objekt
"""Välkommen! Detta program skapar objekt i klasser med tre olika attribut.
Det finns även en modul som kör en felhantering för personnummer."""
import typed_input
lista_studenter = [] # tom lista skapas
class Student:
    def __init__(self, förnamn, efternamn, personnmr):
        """Definerar attributen förnamn, efternamn och personnmr för objektet
        Student."""
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnmr = personnmr
    def __str__(self):
        """Returnerar en sträng som innehåller attributen"""
        return ("Namn: " + self.förnamn + " " + self.efternamn + " Personnmr: " +(self.personnmr))
i = 0
while i < 3: # while-loop som frågar användaren om förnamn, efternamn och personnmr till objektet Student
    p_förnamn = input("Vad är studentens förnamn? " )
    p_efternamn = input("Vad är studentens efternamn? " )
    p_personnmr = typed_input.felHeltal("Vad är studentens personnmr (skriv ÅÅMMDDXXXX)?" ) # kör modul felhantering
    student = Student(p_förnamn, p_efternamn, p_personnmr)
    lista_studenter.append(student) # lägger till strägen från klassen Student till listan
    print("\nObjekt har skapats! \n")
    i += 1
    print("Här är alla sparade objekt:")
for student in lista_studenter:
    print(student) # skriver ut alla element i listan
