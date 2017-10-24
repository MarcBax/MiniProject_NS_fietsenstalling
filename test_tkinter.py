from  tkinter import *
import csv
window = Tk()
window.title("Welkom!")


def HoofdMenu():
    label = Label(window, text="Welkom bij de NS-fietsenstalling!", bg="blue", fg="white")
    label.config(height=1, width=50)
    label.pack(pady=12)

    button_registreren = Button(window, text="fiets registreren", command=SluitScherm1, bg="blue", fg="white")
    button_registreren.config(height=1, width=15)
    button_registreren.pack(pady=0.1)

    button_stallen = Button(window, text="fiets stallen", command=SluitScherm2, bg="blue", fg="white")
    button_stallen.config(height=1, width=15)
    button_stallen.pack(pady=0.1)

    button_ophalenFiets = Button(window, text="fiets ophalen",bg="blue", fg="white")
    button_ophalenFiets.config(height=1, width=15)
    button_ophalenFiets.pack(pady=0.1)

    button_informatie = Button(window, text="informatie ophalen",bg="blue", fg="white")
    button_informatie.config(height=1, width=15)
    button_informatie.pack(pady=0.1)

    button_quit = Button(window, text='sluiten', command=window.quit, bg='red', fg='white')
    button_quit.config(height=1, width=5)
    button_quit.place(x="258", y="174")

def RegistreerMenu():
    global w, e, print_text, fietsnummer_registratie
    print_text="Uw fietsnummer is: " + str(fietsnummer_registratie)
    w = Tk()
    w.title("Registreren!")
    label = Label(w, text="Fiets Registreren", fg="white", bg="blue")
    label.config(height="1", width="50")
    label.pack()

    naam = Label(w, text="Naam:", fg="white", bg="blue")
    naam.config(height="1", width="5")
    naam.place(x="73", y="65")
    e = Entry(w)
    e.place(x="114", y="66")

    naam_2 = Label(w, text= print_text, fg="black", bg="yellow")
    naam_2.config(height="1", width="30")
    naam_2.place(x="0", y="95")

    buttongadoor = Button(w, text="Registreer Gegevens", fg="white", bg="blue", command=schrijven)
    buttongadoor.config(height="1", width="15")
    buttongadoor.place(x="185", y="174")

    buttongaterug = Button(w, text="Ga terug",command=OpenHoofdMenu, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    w.configure(background="yellow")
    w.maxsize(300, 200)
    w.minsize(300, 200)

def schrijven():
    global e
    test = e.get()
    Registreren.registreren(test)
    print("test:", test)
    outfile = open("temp_test_tkinter.txt", "w")
    outfile.write(test)
    outfile.close()

def StalMenu():
    global win
    win = Tk()
    win.title("Stal!")
    label = Label(win, text="Fiets stallen", fg="white", bg="blue")
    label.config(height="1", width="50")
    label.pack()

    buttongadoor = Button(win, text="Stal Fiets", fg="white", bg="blue")
    buttongadoor.config(height="1", width="15")
    buttongadoor.place(x="185", y="174")

    buttongaterug = Button(win, text="Ga terug",command=OpenHoofdMenu, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    win.configure(background="yellow")
    win.maxsize(300, 200)
    win.minsize(300, 200)


def SluitScherm1():
    window.withdraw()
    RegistreerMenu()

def SluitScherm2():
    window.withdraw()
    StalMenu()

def OpenHoofdMenu():
    window.deiconify()
    w.withdraw()
    for gegevens in w.winfo_children():
        gegevens.destroy()
    win.withdraw()
    for gegevens in win.winfo_children():
        gegevens.destroy()

#author: Marc Bax
def registreren(naam_registratie):                                                          #functie voor het registreren van een fiets
    global print_text, fiietsnummer_registratie
    fietsnummer_registratie = 0
    #infile = open('temp_test_tkinter.txt', 'r')
    #naam_registratie = infile.read()
    #print("Naam: ", naam_registratie)
    #if naam_registratie == "":                                          # als de input ""(niks) is stoppen met while-loop
        #break
    if fietsnummer_registratie < 99:                                    # als het fietsnummer kleiner is dan 99
        fietsnummer_registratie += 1
    print_text = "Uw fietsnummer is: ", str(fietsnummer_registratie)
    with open('registratie.csv', 'r') as lezenregistrerencsv:
            regels = lezenregistrerencsv.readlines()                    #iedere regel van registratie.csv lezen en in een lijst zetten
            teller_naam = 0
            for regel in regels:                                            #iedere regel in de lijst van regels doorlezen
                if naam_registratie in regel:                               #als de naam in de regel staat, bij de teller van de naam 1 optellen
                    teller_naam += 1
                else:                                                       #als de naam niet in de regel staat, bij de teller van de naam 1 optellen
                    teller_naam += 0
            if teller_naam == 1:                                            #als de teller van de naam 1 is, dus als de naam in de registratie csv-file staat
                print("Uw naam is al geregistreerd.")
                #continue
    with open('registratie.csv', 'a') as registrerencsv:
        schrijven = csv.writer(registrerencsv, delimiter = ';')
        schrijven.writerow((fietsnummer_registratie, naam_registratie))     #rij schrijven van de inputs

HoofdMenu()
window.configure(background="yellow")
window.maxsize(300,200)
window.minsize(300,200)
window.mainloop()