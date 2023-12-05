import tkinter as tk
from Salladbar import *  # Importera allt från Salladbar.py

class ToggleButton(tk.Button):
    def __init__(self, master=None, ingr=None, **kwargs):
        super().__init__(master, command=self.toggle, **kwargs)
        self.ingr = ingr
        self.selected = False
    
    def toggle(self):
        self.selected = not self.selected
        self.config(relief=tk.SUNKEN if self.selected else tk.RAISED)

class SaladApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Salladbar")

        self.current_frame = None  # Håller reda på aktuellt frame
        self.salladbar_instance = None

        # skapa instanser av värderna för kvitto senare
        self.bästa_match_tk = []
        self.kompletterande_ingredienser_tk = []
        self.valda_ingredienser_tk = []
        self.extra_ingredienser_tk = []
        self.totalpris_tk = 0
        
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
                self.läs_in_salladbar('sallader_KallePåHörnet.json', 'ingredienser_KallePåHörnet.json')
            elif choice == 2:
                self.läs_in_salladbar('sallader_Citysallad.json', 'ingredienser_Citysallad.json')
            # Lägg till fler elif-block för fler salladsbarer

        button1 = tk.Button(self.current_frame, text="Kalle på hörnet", command=lambda: handle_choice(1))
        button1.pack()

        button2 = tk.Button(self.current_frame, text="Citysallad", command=lambda: handle_choice(2))
        button2.pack()

        # Lägg till fler knappar för fler salladsbarer
    
    def läs_in_salladbar(self, sallader_file, ingredients_file):
        self.clear_frame()
        # Skapa en instans av Salladbar-klassen och bearbeta salladval
        self.salladbar_instance = Salladbar()
        self.salladbar_instance.läs_in_sallader(sallader_file)
        self.salladbar_instance.läs_in_ingredienser(ingredients_file)
        self.bearbeta_salladval(self.salladbar_instance)

    
    def bearbeta_salladval(self, salladbar):
        self.clear_frame()
        # Skapar ett nytt frame för salladsbar-GUI
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        # Skapa ett label för välkomstmeddelandet
        welcome_label = tk.Label(self.current_frame, text="Välkommen!", font=("Arial", 18))
        welcome_label.pack()

        # Skapa knappar för att utföra olika val
        create_salad_button = tk.Button(self.current_frame, text="Skapa en egen sallad", command=lambda: self.välj_ingredienser_tk(salladbar))
        create_salad_button.pack()

        change_saladbar_button = tk.Button(self.current_frame, text="Byta salladbar", command=self.visa_huvudmenyn)
        change_saladbar_button.pack()

        exit_button = tk.Button(self.current_frame, text="Avsluta programmet", command=self.root.quit)
        exit_button.pack()
    
    def välj_ingredienser_tk(self, salladbar_instance):
        self.clear_frame()

        # Skapar ett nytt frame för val av ingredienser
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        # Skapa en rubrik för val av ingredienser
        ingredients_label = tk.Label(self.current_frame, text="Välj dina ingredienser:", font=("Arial", 14))
        ingredients_label.grid(row=0, column=0, columnspan=2)  # Placera rubriken i rutnätet

        # Skapa en lista över valda ingredienser
        valda_ingredienser = []

        # Skapa en funktion för att spåra valda ingredienser
        def toggle_selection(ingr_button, ingr):
            if ingr_button.selected:
                valda_ingredienser.append(ingr)
            else:
                valda_ingredienser.remove(ingr) if ingr in valda_ingredienser else None

        # Skapa knappar för varje ingrediens med deras priser och organisera dem i ett rutnät
        num_buttons_per_row = 4  # Antal knappar per rad

        for i, ingredient in enumerate(salladbar_instance.ingredienser, start=1):
            # Skapar en knapp för varje ingrediens
            button_text = f"{ingredient.namn_ingrediens}: {ingredient.ingrediens_pris} kr"
            button = ToggleButton(self.current_frame, ingr=ingredient, text=button_text)
            button.grid(row=1 + i // num_buttons_per_row, column=i % num_buttons_per_row, padx=5, pady=5)  # Använd grid för att placera knapparna i rutnätet
            button.config(command=lambda ingr_button=button, ingr=ingredient: (ingr_button.toggle(), toggle_selection(ingr_button, ingr)))

        self.valda_ingredienser_tk = valda_ingredienser
        # Skapa en knapp för att gå vidare till nästa steg
        next_button = tk.Button(self.current_frame, text="Fortsätt", command=lambda: self.hitta_matchande_sallader_tk(valda_ingredienser))
        next_button.grid(row=(len(salladbar_instance.ingredienser) // num_buttons_per_row) + 2, columnspan=num_buttons_per_row)  # Placera nästa knapp längst ner i rutnätet


    def hitta_matchande_sallader_tk(self, selected_ingredients):
        
        self.clear_frame()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        # Skapa en rubrik för matchning
        matchning_label = tk.Label(self.current_frame, text="Matchande Ingredienser", font=("Arial", 14))
        matchning_label.pack()

        # Skapa en Text-komponent för att visa matchande sallader och totalpris
        text_output = tk.Text(matchning_label, height=10, width=60)
        text_output.pack()

        # Skapa en lista med namnen på de valda ingredienserna
        valda_ingredienser_namn = [ingrediens.namn_ingrediens for ingrediens in selected_ingredients]

        # Letar efter perfekta matchningar där ingredienserna exakt matchar salladens ingredienser
        perfekta_matchningar = [sallad for sallad in self.salladbar_instance.sallader if set(valda_ingredienser_namn) == set(sallad.ingredienser)]
        
        # Visa matchande sallader i Text-komponenten
        if perfekta_matchningar:
            text_output.insert(tk.END, "Här är salladen som exakt matchar dina valda ingredienser:\n")
            for sallad in perfekta_matchningar:
                text_output.insert(tk.END, f"{sallad.namn_sallad}, Pris: {sallad.sallad_pris} kr\n")
            total_pris = perfekta_matchningar[0].sallad_pris  # Priset för den perfekta matchningen
            text_output.insert(tk.END, f"Totalpris för sallad: {total_pris} kr")


        else:
            bästa_match = None
            bästa_match_antal = 0
            bästa_match_pris = float('inf')   
            bästa_match_kompletterande_ingredienser = None  

            for sallad in self.salladbar_instance.sallader:
                matchande_ingredienser = set(valda_ingredienser_namn).intersection(set(sallad.ingredienser))
                kompletterande_ingredienser = set(sallad.ingredienser) - set(valda_ingredienser_namn)
                
                if len(matchande_ingredienser) > bästa_match_antal or (len(matchande_ingredienser) == bästa_match_antal and sallad.sallad_pris < bästa_match_pris):
                    bästa_match = sallad
                    bästa_match_antal = len(matchande_ingredienser)
                    bästa_match_pris = sallad.sallad_pris
                    bästa_match_kompletterande_ingredienser = kompletterande_ingredienser

        valda_ingredienser_pris = sum(ingrediens.ingrediens_pris for ingrediens in selected_ingredients if ingrediens.namn_ingrediens not in bästa_match.ingredienser)

        if not bästa_match_kompletterande_ingredienser:

            add_button.pack_forget()
            cancel_button.pack_forget()
            continue_button.pack()

            text_output.insert(tk.END, f"Bästa matchande sallad är {bästa_match.namn_sallad} med priset {bästa_match.sallad_pris} kr.\n")
            text_output.insert(tk.END, "Du behöver inte lägga till några kompletterande ingredienser eftersom du redan har alla ingredienser i denna sallad.\n")

            bästa_match_pris += valda_ingredienser_pris
            text_output.insert(tk.END, f"Totalkostnaden blir {bästa_match_pris} kr.\n")

            self.bästa_match_tk = [bästa_match]
            self.kompletterande_ingredienser_tk = None
            self.totalpris_tk = bästa_match_pris

        text_output.insert(tk.END, f"Bästa matchande sallad är {bästa_match.namn_sallad} med priset {bästa_match.sallad_pris} kr.\n")
        text_output.insert(tk.END, f"Du kan lägga till dessa ingredienser: {', '.join(bästa_match_kompletterande_ingredienser)}\n")

        def add_additional_ingredients():

            add_button.pack_forget()
            cancel_button.pack_forget()
            continue_button.pack()

            nonlocal bästa_match_pris
            bästa_match_pris += valda_ingredienser_pris
            text_output.insert(tk.END, f"Totalkostnaden blir {bästa_match_pris} kr.\n")

            self.bästa_match_tk = [bästa_match]
            self.kompletterande_ingredienser_tk = bästa_match_kompletterande_ingredienser
            self.totalpris_tk = bästa_match_pris

        def cancel():

            add_button.pack_forget()
            cancel_button.pack_forget()
            continue_button.pack()

            bara_valda_ingredienser_pris = sum(ingrediens.ingrediens_pris for ingrediens in selected_ingredients)
            text_output.insert(tk.END, f"Totalkostnaden blir {bara_valda_ingredienser_pris} kr.\n")

            self.bästa_match_tk = [bästa_match]
            self.kompletterande_ingredienser_tk = None
            self.totalpris_tk = bara_valda_ingredienser_pris
            

        def continue_extra():
            self.choose_extra_ingredients()

        add_button = tk.Button(self.current_frame, text="Lägg till", command=add_additional_ingredients)
        add_button.pack()

        cancel_button = tk.Button(self.current_frame, text="Nej", command=cancel)
        cancel_button.pack()

        continue_button = tk.Button(self.current_frame, text="Fortsätt", command=continue_extra)
       

    def choose_extra_ingredients(self):
        self.clear_frame()

        # Skapa ett nytt frame för valet av extra ingredienser
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        # Skapa en rubrik för valet av extra ingredienser
        extra_label = tk.Label(self.current_frame, text="Vill du lägga till extra ingredienser?", font=("Arial", 14))
        extra_label.pack()

        # Skapa knappar för att välja att lägga till extra ingredienser eller inte
        add_extra_button = tk.Button(self.current_frame, text="Ja, lägg till extra ingredienser", command=lambda: self.extra_ingrediens())
        add_extra_button.pack()

        continue_button = tk.Button(self.current_frame, text="Nej, fortsätt utan extra ingredienser", command=lambda: self.kvitto())
        continue_button.pack()

    def extra_ingrediens(self):

        self.clear_frame()

        # Skapar ett nytt frame för val av ingredienser
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        # Skapa en rubrik för val av ingredienser
        ingredients_label = tk.Label(self.current_frame, text="Välj dina extra ingredienser:", font=("Arial", 14))
        ingredients_label.grid(row=0, column=0, columnspan=2)  # Placera rubriken i rutnätet

        # Skapa en lista över valda ingredienser
        extra_ingredienser = []

        # Skapa en funktion för att spåra valda ingredienser
        def toggle_selection(ingr_button, ingr):
            if ingr_button.selected:
                extra_ingredienser.append(ingr)
            else:
                extra_ingredienser.remove(ingr) if ingr in extra_ingredienser else None

        # Skapa knappar för varje ingrediens med deras priser och organisera dem i ett rutnät
        num_buttons_per_row = 4  # Antal knappar per rad

        for i, ingredient in enumerate(self.salladbar_instance.ingredienser, start=1):
            # Skapar en knapp för varje ingrediens
            button_text = f"{ingredient.namn_ingrediens}: {ingredient.ingrediens_pris} kr"
            button = ToggleButton(self.current_frame, ingr=ingredient, text=button_text)
            button.grid(row=1 + i // num_buttons_per_row, column=i % num_buttons_per_row, padx=5, pady=5)  # Använd grid för att placera knapparna i rutnätet
            button.config(command=lambda ingr_button=button, ingr=ingredient: (ingr_button.toggle(), toggle_selection(ingr_button, ingr)))

        self.extra_ingredienser_tk = extra_ingredienser
        # Skapa en knapp för att gå vidare till nästa steg
        next_button = tk.Button(self.current_frame, text="Fortsätt", command=lambda: self.kvitto())
        next_button.grid(row=(len(self.salladbar_instance.ingredienser) // num_buttons_per_row) + 2, columnspan=num_buttons_per_row)  # Placera nästa knapp längst ner i rutnätet
        
    def kvitto(self):
        self.clear_frame()
        
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        # Skapa en rubrik för matchning
        kvitto_label = tk.Label(self.current_frame, text="Matchande Ingredienser", font=("Arial", 14))
        kvitto_label.pack()

        # Skapa en Text-komponent för att visa matchande sallader och totalpris
        text_output = tk.Text(kvitto_label, height=20, width=80)
        text_output.pack()

        with open('kvitto.txt', 'w', encoding='utf-8') as f:
            f.write("""
                    HÄR ÄR DITT KVITTO:
                    """)
            print("""
              HÄR ÄR DITT KVITTO: \n
              """)
            text_output.insert(tk.END, f"""
                                HÄR ÄR DITT KVITTO: \n
                               """)
            
            f.write("\nValda ingredienser:\n")
            print("\nValda ingredienser:\n")
            text_output.insert(tk.END, f"\nValda ingredienser:\n")
            for ingrediens in self.valda_ingredienser_tk:
                f.write(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr\n")
                print(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr")
                text_output.insert(tk.END, f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr\n")

            if self.extra_ingredienser_tk:
                f.write("\nExtra ingredienser:\n")
                print("\nExtra ingredienser:")
                text_output.insert(tk.END, f"\nExtra ingredienser:\n")

                for ingrediens in self.extra_ingredienser_tk:
                    f.write(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr\n")
                    print(f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr")
                    text_output.insert(tk.END, f"{ingrediens.namn_ingrediens}: {ingrediens.ingrediens_pris} kr\n")
                    self.totalpris_tk += ingrediens.ingrediens_pris
            
            f.write("\nBästa matchning:\n")
            print("\nBästa matchning:")
            text_output.insert(tk.END, f"\nBästa matchning:\n")
            for sallad in self.bästa_match_tk:
                f.write(f"{sallad.namn_sallad}: {sallad.sallad_pris} kr\n")
                print(f"{sallad.namn_sallad}: {sallad.sallad_pris} kr")
                text_output.insert(tk.END, f"{sallad.namn_sallad}: {sallad.sallad_pris} kr\n")
            
            if self.kompletterande_ingredienser_tk:
                f.write("\nKompletterande ingredienser:\n")
                print("\nKompletterande ingredienser:")
                text_output.insert(tk.END, f"\nKompletterande ingredienser:\n")
                for ingrediens in self.kompletterande_ingredienser_tk:
                    f.write(f"{ingrediens}\n")
                    print(ingrediens)
                    text_output.insert(tk.END, f"{ingrediens}\n")
            
            f.write(f"\nTotalt pris: {self.totalpris_tk} kr\n")
            print(f"\nTotal pris: {self.totalpris_tk} kr\n")
            text_output.insert(tk.END, f"\nTotal pris: {self.totalpris_tk} kr\n")

            ny_button = tk.Button(self.current_frame, text="Skapa en ny sallad", command=lambda: self.bearbeta_salladval(self.salladbar_instance))
            ny_button.pack()

            avsluta_button = tk.Button(self.current_frame, text="Avsluta program", command=self.root.quit)
            avsluta_button.pack()

            
        


    

def main():
    root = tk.Tk()
    app = SaladApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
