import tkinter as tk
from Salladbar import *  # Importera Salladbar-klassen från Salladbar.py

class SaladApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Salladbar")

        self.current_frame = None  # Håller reda på aktuellt frame
        
        # Skapa en hälsningstext
        self.greeting = tk.Label(root, text="Välkommen till SalladApp!", font=("Arial", 18))
        self.greeting.pack(pady=20)
        
        # Knapp för att fortsätta till nästa steg (visa huvudmenyn)
        self.next_button = tk.Button(root, text="Välj salladsbar", command=self.visa_huvudmenyn)
        self.next_button.pack()
    
    def clear_frame(self):
        """Rensar det aktuella frame."""
        if self.current_frame:
            self.current_frame.destroy()

    def visa_huvudmenyn(self):
        self.next_button.destroy()
        self.clear_frame()

        # Skapar ett nytt frame för huvudmenyn
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        # Skapar ett label för välkomstmeddelandet
        welcome_label = tk.Label(self.current_frame, text="Välkommen! Välj vilken salladsbar du vill besöka:")
        welcome_label.pack()

        # Skapar knappar för varje salladsbar
        def handle_choice(choice):
            if choice == 1:
                self.load_saladbar('sallader_KallePåHörnet.json', 'ingredienser_KallePåHörnet.json')
            elif choice == 2:
                self.load_saladbar('sallader_Citysallad.json', 'ingredienser_Citysallad.json')
            # Lägg till fler elif-block för fler salladsbarer

        button1 = tk.Button(self.current_frame, text="Kalle på hörnet", command=lambda: handle_choice(1))
        button1.pack()

        button2 = tk.Button(self.current_frame, text="Citysallad", command=lambda: handle_choice(2))
        button2.pack()

        # Lägg till fler knappar för fler salladsbarer
    
    def load_saladbar(self, sallader_file, ingredients_file):
        self.clear_frame()
        # Skapa en instans av Salladbar-klassen och bearbeta salladval
        salladbar_instance = Salladbar()
        salladbar_instance.läs_in_sallader(sallader_file)
        salladbar_instance.läs_in_ingredienser(ingredients_file)
        self.bearbeta_salladval(salladbar_instance)

    
    def bearbeta_salladval(self, salladbar):
        # Skapar ett nytt frame för salladsbar-GUI
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        # Skapa ett label för välkomstmeddelandet
        welcome_label = tk.Label(self.current_frame, text="Välkommen!", font=("Arial", 18))
        welcome_label.pack()

        # Skapa knappar för att utföra olika val
        create_salad_button = tk.Button(self.current_frame, text="Skapa en egen sallad", command=lambda: self.create_salad(salladbar))
        create_salad_button.pack()

        change_saladbar_button = tk.Button(self.current_frame, text="Byta salladbar", command=self.visa_huvudmenyn)
        change_saladbar_button.pack()

        exit_button = tk.Button(self.current_frame, text="Avsluta programmet", command=self.root.quit)
        exit_button.pack()



def main():
    root = tk.Tk()
    app = SaladApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
