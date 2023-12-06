import tkinter as tk
from Salladbar import *  # Importera allt från Salladbar.py

class ToggleButton(tk.Button):
    '''
    En specialiserad knapp för att växla mellan vald och icke-vald status.
    '''
    def __init__(self, master=None, ingr=None, **kwargs):
        super().__init__(master, command=self.toggle, **kwargs)
        self.ingr = ingr
        self.selected = False
    
    def toggle(self):
        '''
        Växlar mellan vald och icke-vald status och ändrar knappens utseende.
        '''
        self.selected = not self.selected
        self.config(relief=tk.SUNKEN if self.selected else tk.RAISED)

class SaladApp:
    '''
    Huvudapplikationsklassen för SalladApp.
    '''

    def __init__(self, root):
        '''
        Initierar huvudapplikationen med en hälsningstext och knapp för att visa huvudmenyn.
        '''
        self.root = root
        self.root.title("Salladbar")

        '''
        Håller reda på aktuellt frame
        '''
        self.nuvarande_frame = None  
        
        '''
        skapa instanser av värderna för kvitto senare
        '''
        self.salladbar_instans = None
        self.bästa_match_tk = []
        self.kompletterande_ingredienser_tk = []
        self.valda_ingredienser_tk = []
        self.extra_ingredienser_tk = []
        self.totalpris_tk = 0
        

        self.hälsning = tk.Label(root, text="Välkommen till SalladApp!", font=("Arial", 18))
        self.hälsning.pack(pady=20)
        
        
        self.nästa_knapp = tk.Button(root, text="Välj salladsbar", command=self.visa_huvudmenyn)
        self.nästa_knapp.pack()
    
    def rensa_skapa_frame(self):
        '''
        Rensar det aktuella frame.
        '''
        if self.nuvarande_frame:
            self.nuvarande_frame.destroy()

        '''
        Skapar ett nytt frame.
        '''
        self.nuvarande_frame = tk.Frame(self.root)
        self.nuvarande_frame.pack()

    def visa_huvudmenyn(self):
        '''
        Visar huvudmenyn med knappar för att välja salladsbar.
        '''
        
        self.nästa_knapp.destroy()
        self.rensa_skapa_frame()

        
        välkomst_label = tk.Label(self.nuvarande_frame, text="Välkommen! Välj vilken salladsbar du vill besöka:")
        välkomst_label.pack()

        # Skapar knappar för varje salladsbar
        def salladbar_val(choice):
            if choice == 1:
                self.läs_in_salladbar('sallader_KallePåHörnet.json', 'ingredienser_KallePåHörnet.json')
            elif choice == 2:
                self.läs_in_salladbar('sallader_Citysallad.json', 'ingredienser_Citysallad.json')
            # Lägg till fler elif-block för fler salladsbarer

        salladbar1 = tk.Button(self.nuvarande_frame, text="Kalle på hörnet", command=lambda: salladbar_val(1))
        salladbar1.pack()

        salladbar2 = tk.Button(self.nuvarande_frame, text="Citysallad", command=lambda: salladbar_val(2))
        salladbar2.pack()
        # Lägg till fler knappar för fler salladsbarer
    
    def läs_in_salladbar(self, sallader_file, ingrediens_file):
        '''
        Läser in salladsbarinformation från filer och bearbetar vald sallad.
        '''
        self.rensa_skapa_frame()
        
        # Skapa en instans av Salladbar-klassen och bearbeta salladval
        self.salladbar_instans = Salladbar()
        self.salladbar_instans.läs_in_sallader(sallader_file)
        self.salladbar_instans.läs_in_ingredienser(ingrediens_file)
        self.bearbeta_salladval(self.salladbar_instans)

    
    def bearbeta_salladval(self, salladbar):
        '''
        Hanterar val av salladbar och visar alternativ för användaren.
        '''

        self.rensa_skapa_frame()
        
        # Skapa ett label för välkomstmeddelandet
        välkomst_label = tk.Label(self.nuvarande_frame, text="Välkommen!", font=("Arial", 18))
        välkomst_label.pack()

        # Skapa knappar för att utföra olika val
        skappa_sallad_knapp = tk.Button(self.nuvarande_frame, text="Skapa en egen sallad", command=lambda: self.välj_ingredienser_tk(salladbar))
        skappa_sallad_knapp.pack()

        byt_salladbar_knapp = tk.Button(self.nuvarande_frame, text="Byta salladbar", command=self.visa_huvudmenyn)
        byt_salladbar_knapp.pack()

        avsluta_knapp = tk.Button(self.nuvarande_frame, text="Avsluta programmet", command=self.root.quit)
        avsluta_knapp.pack()
    
    def välj_ingredienser_tk(self, salladbar_instans):
        '''
        Visar gränssnittet för att välja ingredienser.
        '''
        self.rensa_skapa_frame()

        # Skapa en rubrik för val av ingredienser
        ingrediens_label = tk.Label(self.nuvarande_frame, text="Välj dina ingredienser:", font=("Arial", 14))
        ingrediens_label.grid(row=0, column=0, columnspan=2)  # Placera rubriken i rutnätet

        # Skapa en lista över valda ingredienser
        valda_ingredienser = []

        # Skapa en funktion för att spåra valda ingredienser
        def toggle_selection(ingr_knapp, ingr):
            if ingr_knapp.selected:
                valda_ingredienser.append(ingr)
            else:
                valda_ingredienser.remove(ingr) if ingr in valda_ingredienser else None

        # Skapa knappar för varje ingrediens med deras priser och organisera dem i ett rutnät
        antal_knappar_per_rad = 4 

        for i, ingredient in enumerate(salladbar_instans.ingredienser, start=1):
            # Skapar en knapp för varje ingrediens
            knapp_text = f"{ingredient.namn_ingrediens}: {ingredient.ingrediens_pris} kr"
            knapp = ToggleButton(self.nuvarande_frame, ingr=ingredient, text=knapp_text)
            knapp.grid(row=1 + i // antal_knappar_per_rad, column=i % antal_knappar_per_rad, padx=5, pady=5)  # Använd grid för att placera knapparna i rutnätet
            knapp.config(command=lambda ingr_knapp=knapp, ingr=ingredient: (ingr_knapp.toggle(), toggle_selection(ingr_knapp, ingr)))

        self.valda_ingredienser_tk = valda_ingredienser
        # Skapa en knapp för att gå vidare till nästa steg
        nästa_knapp = tk.Button(self.nuvarande_frame, text="Fortsätt", command=lambda: self.hitta_matchande_sallader_tk(valda_ingredienser))
        nästa_knapp.grid(row=(len(salladbar_instans.ingredienser) // antal_knappar_per_rad) + 2, columnspan=antal_knappar_per_rad)  # Placera nästa knapp längst ner i rutnätet


    def hitta_matchande_sallader_tk(self, selected_ingrediens):
        '''
        Hittar den salladen som matchar de valda ingredienserna.
        '''
        
        self.rensa_skapa_frame()

        self.nuvarande_frame = tk.Frame(self.root)
        self.nuvarande_frame.pack()

        # Skapa en rubrik för matchning
        matchning_label = tk.Label(self.nuvarande_frame, text="Matchande Ingredienser", font=("Arial", 14))
        matchning_label.pack()

        # Skapa en Text-komponent för att visa matchande sallader och totalpris
        text_output = tk.Text(matchning_label, height=10, width=60)
        text_output.pack()

        valda_ingredienser_namn = [ingrediens.namn_ingrediens for ingrediens in selected_ingrediens]

        '''
        Letar efter perfekta matchningar där ingredienserna exakt matchar salladens ingredienser
        '''
        perfekta_matchningar = [sallad for sallad in self.salladbar_instans.sallader if set(valda_ingredienser_namn) == set(sallad.ingredienser)]
        
        # Visa matchande sallader i Text-komponenten
        if perfekta_matchningar:
            text_output.insert(tk.END, "Här är salladen som exakt matchar dina valda ingredienser:\n")
            for sallad in perfekta_matchningar:
                text_output.insert(tk.END, f"{sallad.namn_sallad}, Pris: {sallad.sallad_pris} kr\n")
            total_pris = perfekta_matchningar[0].sallad_pris  # Priset för den perfekta matchningen
            text_output.insert(tk.END, f"Totalpris för sallad: {total_pris} kr")

            '''
            Om det inte finns perfekta matchningar
            '''
        else:
            '''
            Initialiserar variabler för att spåra bästa matchande salladen
            '''
            bästa_match = None
            bästa_match_antal = 0
            bästa_match_pris = float('inf')   
            bästa_match_kompletterande_ingredienser = None  

            '''
            Loopar genom alla sallader för att hitta den bästa matchningen
            '''
            for sallad in self.salladbar_instans.sallader:
                matchande_ingredienser = set(valda_ingredienser_namn).intersection(set(sallad.ingredienser))
                kompletterande_ingredienser = set(sallad.ingredienser) - set(valda_ingredienser_namn)
                
                '''
                Uppdaterar variabler om en bättre matchande sallad hittas
                '''
                if len(matchande_ingredienser) > bästa_match_antal or (len(matchande_ingredienser) == bästa_match_antal and sallad.sallad_pris < bästa_match_pris):
                    bästa_match = sallad
                    bästa_match_antal = len(matchande_ingredienser)
                    bästa_match_pris = sallad.sallad_pris
                    bästa_match_kompletterande_ingredienser = kompletterande_ingredienser

        '''
        Beräknar priset för de valda ingredienserna som inte redan finns i den bästa matchande salladen
        '''
        valda_ingredienser_pris = sum(ingrediens.ingrediens_pris for ingrediens in selected_ingrediens if ingrediens.namn_ingrediens not in bästa_match.ingredienser)

        if not bästa_match_kompletterande_ingredienser:

            add_button.pack_forget()
            lägg_inte_till_kompletterande_ingredienser_button.pack_forget()
            continue_button.pack()

            text_output.insert(tk.END, f"Bästa matchande sallad är {bästa_match.namn_sallad} med priset {bästa_match.sallad_pris} kr.\n")
            text_output.insert(tk.END, "Du behöver inte lägga till några kompletterande ingredienser eftersom du redan har alla ingredienser i denna sallad.\n")

            bästa_match_pris += valda_ingredienser_pris
            text_output.insert(tk.END, f"Totalkostnaden blir {bästa_match_pris} kr.\n")

            self.bästa_match_tk = [bästa_match]
            self.kompletterande_ingredienser_tk = None
            self.totalpris_tk = bästa_match_pris

        '''
        Om det finns kompletterande ingredienser att lägga till
        '''
        text_output.insert(tk.END, f"Bästa matchande sallad är {bästa_match.namn_sallad} med priset {bästa_match.sallad_pris} kr.\n")
        text_output.insert(tk.END, f"Du kan lägga till dessa ingredienser: {', '.join(bästa_match_kompletterande_ingredienser)}\n")

        
        '''
        Användarinteraktion för att lägga till kompletterande ingredienser
        '''
        def lägg_till_kompletterande_ingredienser():

            add_button.pack_forget()
            lägg_inte_till_kompletterande_ingredienser_button.pack_forget()
            continue_button.pack()

            nonlocal bästa_match_pris
            bästa_match_pris += valda_ingredienser_pris
            text_output.insert(tk.END, f"Totalkostnaden blir {bästa_match_pris} kr.\n")

            self.bästa_match_tk = [bästa_match]
            self.kompletterande_ingredienser_tk = bästa_match_kompletterande_ingredienser
            self.totalpris_tk = bästa_match_pris

        def lägg_inte_till_kompletterande_ingredienser():

            add_button.pack_forget()
            lägg_inte_till_kompletterande_ingredienser_button.pack_forget()
            continue_button.pack()

            bara_valda_ingredienser_pris = sum(ingrediens.ingrediens_pris for ingrediens in selected_ingrediens)
            text_output.insert(tk.END, f"Totalkostnaden blir {bara_valda_ingredienser_pris} kr.\n")

            self.bästa_match_tk = [bästa_match]
            self.kompletterande_ingredienser_tk = None
            self.totalpris_tk = bara_valda_ingredienser_pris
            

        def fortsätt_till_extra():
            self.val_extra_ingrediens()

        add_button = tk.Button(self.nuvarande_frame, text="Lägg till", command=lägg_till_kompletterande_ingredienser)
        add_button.pack()

        lägg_inte_till_kompletterande_ingredienser_button = tk.Button(self.nuvarande_frame, text="Nej", command=lägg_inte_till_kompletterande_ingredienser)
        lägg_inte_till_kompletterande_ingredienser_button.pack()

        continue_button = tk.Button(self.nuvarande_frame, text="Fortsätt", command=fortsätt_till_extra)
       

    def val_extra_ingrediens(self):
        '''
        Visar alternativ för att välja extra ingredienser.
        '''
        self.rensa_skapa_frame()

        # Skapa en rubrik för valet av extra ingredienser
        extra_label = tk.Label(self.nuvarande_frame, text="Vill du lägga till extra ingredienser?", font=("Arial", 14))
        extra_label.pack()

        # Skapa knappar för att välja att lägga till extra ingredienser eller inte
        add_extra_button = tk.Button(self.nuvarande_frame, text="Ja, lägg till extra ingredienser", command=lambda: self.extra_ingrediens())
        add_extra_button.pack()

        continue_button = tk.Button(self.nuvarande_frame, text="Nej, fortsätt utan extra ingredienser", command=lambda: self.kvitto())
        continue_button.pack()

    def extra_ingrediens(self):
        '''
        Hanterar val av extra ingredienser.
        '''

        self.rensa_skapa_frame()

        # Skapa en rubrik för val av ingredienser
        ingrediens_label = tk.Label(self.nuvarande_frame, text="Välj dina extra ingredienser:", font=("Arial", 14))
        ingrediens_label.grid(row=0, column=0, columnspan=2)  # Placera rubriken i rutnätet

        # Skapa en lista över valda ingredienser
        extra_ingredienser = []

        # Skapa en funktion för att spåra valda ingredienser
        def toggle_selection(ingr_knapp, ingr):
            if ingr_knapp.selected:
                extra_ingredienser.append(ingr)
            else:
                extra_ingredienser.remove(ingr) if ingr in extra_ingredienser else None

        # Skapa knappar för varje ingrediens med deras priser och organisera dem i ett rutnät
        antal_knappar_per_rad = 4  # Antal knappar per rad

        for i, ingredient in enumerate(self.salladbar_instans.ingredienser, start=1):
            # Skapar en knapp för varje ingrediens
            knapp_text = f"{ingredient.namn_ingrediens}: {ingredient.ingrediens_pris} kr"
            knapp = ToggleButton(self.nuvarande_frame, ingr=ingredient, text=knapp_text)
            knapp.grid(row=1 + i // antal_knappar_per_rad, column=i % antal_knappar_per_rad, padx=5, pady=5)  # Använd grid för att placera knapparna i rutnätet
            knapp.config(command=lambda ingr_knapp=knapp, ingr=ingredient: (ingr_knapp.toggle(), toggle_selection(ingr_knapp, ingr)))

        self.extra_ingredienser_tk = extra_ingredienser
        # Skapa en knapp för att gå vidare till nästa steg
        nästa_knapp = tk.Button(self.nuvarande_frame, text="Fortsätt", command=lambda: self.kvitto())
        nästa_knapp.grid(row=(len(self.salladbar_instans.ingredienser) // antal_knappar_per_rad) + 2, columnspan=antal_knappar_per_rad)  # Placera nästa knapp längst ner i rutnätet
        
    def kvitto(self):
        '''
        Visar kvittot för användaren baserat på valda ingredienser och matchningar.
        '''

        self.rensa_skapa_frame()

        # Skapa en rubrik för matchning
        kvitto_label = tk.Label(self.nuvarande_frame, text="Matchande Ingredienser", font=("Arial", 14))
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

            ny_button = tk.Button(self.nuvarande_frame, text="Skapa en ny sallad", command=lambda: self.bearbeta_salladval(self.salladbar_instans))
            ny_button.pack()

            avsluta_button = tk.Button(self.nuvarande_frame, text="Avsluta program", command=self.root.quit)
            avsluta_button.pack()    

def main():
    root = tk.Tk()
    app = SaladApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
