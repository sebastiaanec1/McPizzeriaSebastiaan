# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in: MC Pizzeria
#
#
# Vul hier jullie namen in: Sebastiaan
#
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------
def zoekKlant():
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    print(gevonden_klanten) 
    invoerveldKlantnaam.delete(0, END) 
    invoerveldKlantNr.delete(0, END) 
    for rij in gevonden_klanten: 
        invoerveldKlantNr.insert(END, rij[0])
        invoerveldKlantnaam.insert(END, rij[1])    

 
            
### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")
knopSluit = Button(venster, text="Afsluiten", width=15, command=venster.destroy)
knopSluit.grid(row=17, column=4)

LabelKlantnaam = Label(venster, text="klantnaam")
LabelKlantnaam.grid(row=1, column=0)
ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")
KnopZoekOpKlantnaam = Button(venster, text="Zoek klant", width=12, command=zoekKlant)
KnopZoekOpKlantnaam.grid(row=1, column=4, sticky="W")

LabelKlantNr = Label(venster, text="klantnummer")
LabelKlantNr.grid(row=2, column=0)
invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")


labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")









#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
