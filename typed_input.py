def läs_in_flyttal(prompt):
    '''
    Läser in ett flyttal från användaren med angivet prompt.
    '''
    while True:
        try:
            värde = float(input(prompt)) 
            '''
            En sträng som innehåller meddelandet som visas för användaren för att instruera dem att mata in ett flyttal.
            '''
            return värde 
        except ValueError:
            print("Det där var inte ett flyttal. Försök igen.")
            '''
            Om användaren matar in något som inte kan tolkas som ett giltigt flyttal, 
            kommer funktionen att kasta ett ValueError och skriva ut ett felmeddelande.
            '''

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
