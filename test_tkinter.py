from  tkinter import *
import csv
import datetime
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

    button_ophalenFiets = Button(window, text="fiets ophalen", command=SluitScherm3,bg="blue", fg="white")
    button_ophalenFiets.config(height=1, width=15)
    button_ophalenFiets.pack(pady=0.1)

    button_informatie = Button(window, text="informatie ophalen",command=SluitScherm4,bg="blue", fg="white")
    button_informatie.config(height=1, width=15)
    button_informatie.pack(pady=0.1)

    button_quit = Button(window, text='sluiten', command=window.quit, bg='red', fg='white')
    button_quit.config(height=1, width=5)
    button_quit.place(x="258", y="174")

def RegistreerMenu():
    global w, e, fietsnummer_registratie
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

    if fietsnummer_registratie < 99:
        fietsnummer_registratie += 1
        print_text = 'Uw fietsnummer is: ' + str(fietsnummer_registratie)
    else:
        print_text = "Het maximaal aantal fietsen is gestald."
    naam_2 = Label(w, text= print_text, fg="black", bg="yellow")
    naam_2.config(height="1", width="30")
    naam_2.place(x="0", y="95")

    naam_registratie = e.get()
    print("Naam: ", str(naam_registratie))
    buttongadoor = Button(w, text="Registreer Gegevens", fg="white", bg="blue", command=Registratie)
    buttongadoor.config(height="1", width="15")
    buttongadoor.place(x="185", y="174")

    buttongaterug = Button(w, text="Ga terug",command=OpenHoofdMenu, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    w.configure(background="yellow")
    w.maxsize(300, 200)
    w.minsize(300, 200)

def Registratie():
    schrijven_registreren()
    OpenHoofdMenu()

def schrijven_registreren():
    global e
    naam = e.get()
    registreren(naam)

def StalMenu():
    global win, e1, e2
    win = Tk()
    win.title("Stal!")
    label = Label(win, text="Fiets stallen", fg="white", bg="blue")
    label.config(height="1", width="50")
    label.pack()

    naam = Label(win, text="Naam:", fg="white", bg="blue")
    naam.config(height="1", width="12")
    naam.place(x="43", y="65")
    e1 = Entry(win)
    e1.place(x="138", y="66")

    fietsNummer = Label(win, text="Fiets nummer:", fg="white", bg="blue")
    fietsNummer.config(height="1", width="12")
    fietsNummer.place(x="43", y="85")
    e2 = Entry(win)
    e2.place(x="138", y="86")

    buttongadoor = Button(win, text="Stal Fiets", fg="white", bg="blue", command=Stallen)
    buttongadoor.config(height="1", width="15")
    buttongadoor.place(x="185", y="174")

    buttongaterug = Button(win, text="Ga terug",command=OpenHoofdMenu1, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    win.configure(background="yellow")
    win.maxsize(300, 200)
    win.minsize(300, 200)

def Stallen():
    schrijven_stallen()
    OpenHoofdMenu1()

def schrijven_stallen():
    global e1, e2
    naam = e1.get()
    fietsnummer = e2.get()
    stallen(naam, fietsnummer)

# auteur: Mark
def OphaalMenu():
    global wind, e5, e6
    wind = Tk()
    wind.title("Ophalen!")
    label = Label(wind, text="Fiets ophalen", fg="white", bg="blue")
    label.config(height="1", width="50")
    label.pack()

    naam = Label(wind, text="Naam:", fg="white", bg="blue")
    naam.config(height="1", width="12")
    naam.place(x="43", y="65")
    e5 = Entry(wind)
    e5.place(x="138", y="66")

    fietsNummer = Label(wind, text="Fiets nummer:", fg="white", bg="blue")
    fietsNummer.config(height="1", width="12")
    fietsNummer.place(x="43", y="85")
    e6 = Entry(wind)
    e6.place(x="138", y="86")

    buttongadoor = Button(wind, text="haal op", fg="white", bg="blue", command=Ophalen)
    buttongadoor.config(height="1", width="15")
    buttongadoor.place(x="185", y="174")

    buttongaterug = Button(wind, text="Ga terug",command=OpenHoofdMenu2, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    wind.configure(background="yellow")
    wind.maxsize(300, 200)
    wind.minsize(300, 200)

def Ophalen():
    schrijven_ophalen()
    OpenHoofdMenu2()

def schrijven_ophalen():
    global e5, e6
    naam = e5.get()
    fietsnummer = e6.get()
    ophalen(naam, fietsnummer)

# auteur: Mark
def InfoMenu():
    global windo
    windo = Tk()
    windo.title("Informatie!")
    label = Label(windo, text="Informatie", fg="white", bg="blue")
    label.config(height="1", width="50")
    label.pack()

    info = Label(windo, text="Deze fietsen stalling heeft 99 plekken \n en is 24/7 open.", fg="black", bg="yellow")
    info.config(height="2", width="30")
    info.pack()

    buttongadoor = Button(windo, text="persoonlijke informatie", fg="white", bg="blue", command=Open_persoonlijke_informatie)
    buttongadoor.config(height="1", width="18")
    buttongadoor.place(x="169", y="174")

    buttongaterug = Button(windo, text="Ga terug",command=OpenHoofdMenu3, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    windo.configure(background="yellow")
    windo.maxsize(300, 200)
    windo.minsize(300, 200)

def Open_persoonlijke_informatie():
    windo.withdraw()
    Persoonlijke_informatie()

def Persoonlijke_informatie():
    global window1, e3, e4
    window1 = Tk()
    window1.title("Informatie!")
    label = Label(windo, text="Informatie", fg="white", bg="blue")
    label.config(height="1", width="50")
    label.pack()

    naam = Label(window1, text="Naam:", fg="white", bg="blue")
    naam.config(height="1", width="12")
    naam.place(x="43", y="65")
    e3 = Entry(window1)
    e3.place(x="138", y="66")

    fietsNummer = Label(window1, text="Fiets nummer:", fg="white", bg="blue")
    fietsNummer.config(height="1", width="12")
    fietsNummer.place(x="43", y="85")
    e4 = Entry(window1)
    e4.place(x="138", y="86")

    buttongadoor = Button(window1, text="opvragen", fg="white", bg="blue",command=aanroepen_informatie)
    buttongadoor.config(height="1", width="18")
    buttongadoor.place(x="169", y="174")

    buttongaterug = Button(window1, text="Ga terug", command=OpenHoofdMenu4, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    window1.configure(background="yellow")
    window1.maxsize(300, 200)
    window1.minsize(300, 200)

def aanroepen_informatie():
    schrijven_persoonlijke_informatie()
    pop_up_informatie_datum()

def schrijven_persoonlijke_informatie():
    global e3, e4
    naam = e3.get()
    fietsnummer = e4.get()
    informatie_opvragen(naam, fietsnummer)

def pop_up_informatie_datum():
    global datum
    window2 = Tk()
    window2.title("Informatie!")
    label = Label(windo, text="Datum", fg="white", bg="blue")
    label.config(height="1", width="50")
    label.pack()

    naam_3 = Label(window2, text=datum, fg="black", bg="yellow")
    naam_3.config(height="1", width="30")
    naam_3.pack()

    #buttongaterug = Button(window2, text="sluiten", command=?, fg="white", bg="red")
    #buttongaterug.config(height="1", width="15")
    #buttongaterug.place(x="0", y="174")

    window2.configure(background="yellow")
    window2.maxsize(75, 25)
    window2.minsize(75, 25)

#auteur: Mark
def SluitScherm1():
    window.withdraw()
    RegistreerMenu()

#auteur: Mark
def SluitScherm2():
    window.withdraw()
    StalMenu()

# auteur: Mark
def SluitScherm3():
   window.withdraw()
   OphaalMenu()

# auteur: Mark
def SluitScherm4():
    window.withdraw()
    InfoMenu()

def OpenHoofdMenu():
    window.deiconify()
    w.withdraw()
    for gegevens in w.winfo_children():
        gegevens.destroy()

# auteur: Mark
def OpenHoofdMenu1():
    window.deiconify()
    win.withdraw()
    for gegevens in win.winfo_children():
        gegevens.destroy()

# auteur: Mark
def OpenHoofdMenu2():
    window.deiconify()
    wind.withdraw()
    for gegevens in wind.winfo_children():
        gegevens.destroy()

# auteur: Mark
def OpenHoofdMenu3():
    window.deiconify()
    windo.withdraw()
    for gegevens in windo.winfo_children():
        gegevens.destroy()

def OpenHoofdMenu4():
    window.deiconify()
    window1.withdraw()
    for gegevens in window1.winfo_children():
        gegevens.destroy()

#auteur: Marc Bax
def registreren(naam_registratie):              #functie voor het registreren van een fiets
    global fietsnummer_registratie
    #infile = open('temp_test_tkinter.txt', 'r')
    #naam_registratie = infile.read()
    #print("Naam: ", naam_registratie)
    #if naam_registratie == "":                                          # als de input ""(niks) is stoppen met while-loop
        #break
    #with open('registratie.csv', 'r') as lezenregistrerencsv:
            #regels = lezenregistrerencsv.readlines()                    #iedere regel van registratie.csv lezen en in een lijst zetten
            #teller_naam = 0
            #for regel in regels:                                            #iedere regel in de lijst van regels doorlezen
                #if naam_registratie in regel:                               #als de naam in de regel staat, bij de teller van de naam 1 optellen
                    #teller_naam += 1
                #else:                                                       #als de naam niet in de regel staat, bij de teller van de naam 1 optellen
                    #teller_naam += 0
            #if teller_naam == 1:                                            #als de teller van de naam 1 is, dus als de naam in de registratie csv-file staat
                #print("Uw naam is al geregistreerd.")
                #continue
    with open('registratie.csv', 'a') as registrerencsv:
        schrijven = csv.writer(registrerencsv, delimiter = ';')
        print(naam_registratie)
        schrijven.writerow((fietsnummer_registratie, naam_registratie))     #rij schrijven van de inputs

#auteur: Marc Bax
def stallen(naam_stallen, fietsnummer_stallen):                           #functie voor het stallen van een fiets
    global datum_tijd
    with open('stallen.csv', 'a') as stallencsv:
        vandaag = datetime.datetime.today()
        datum_tijd = vandaag.strftime("%a %x %X")                           #de huidige datum en tijd
        schrijven = csv.writer(stallencsv, delimiter = ';')
        schrijven.writerow((fietsnummer_stallen, naam_stallen, datum_tijd))       #in stallen.csv de variable schrijven

#auteur: Gianluca
def ophalen(naam_ophalen, fietsnummer_ophalen):
    global datum_tijd
    lijst_gestalde_fietsen = []  # lijst maken voor controle naam en nummer
    lijst_opgehaald_fietsen = []  # lijst maken voor nacontrole
    with open('stallen.csv', 'r') as lezenstallencsv:  # naar lijst schrijven
        regels = lezenstallencsv.readlines()
        for rij in regels:
            lijst_gestalde_fietsen.append(rij)
        #teller = 0
        #for item in lijst_gestalde_fietsen:  # door lijst heen loopen om gebruiker te vinden
        #    if fietsnummer_ophalen in item and naam_ophalen in item:  # gebruiker in lijst zorgt voor een positief getal
        #        teller += 1
        #if teller > 0:
        #    lijst_opgehaald_fietsen.append(fietsnummer_ophalen + ";" + naam_ophalen + ";" + datum_tijd)  # bij een positief getal mag fiets opgehaald worden
        #    # en wordt de gebruiker in een lijst van ophehaalde fietsen gestopt
        #    print("u mag uw fiets ophalen.")
        #else:  # bij een gebrek aan positief getal krijgt gebruiker een foutmelding
        #    if teller < 1:
        #        print("onjuiste combinatie")
    #print(lijst_gestalde_fietsen)
    #print(lijst_opgehaald_fietsen)
        for row in regels:
            if naam_ophalen in row and fietsnummer_ophalen in row:
                lijst_gestalde_fietsen.remove(row)
    with open('stallen.csv', 'w') as schrijvenstallencsv:
        schrijven = csv.writer(schrijvenstallencsv)
        schrijven.writerow("fietsnummer;naam;datum")
        schrijven.writerow((lijst_gestalde_fietsen))

#auteur: Marc Bax
def informatie_opvragen(naam_informatie, fietsnummer_informatie):
    global datum
    with open('stallen.csv', 'r') as lezenstallencsv:
        lezen = csv.reader(lezenstallencsv, delimiter=';')
        if naam_informatie or fietsnummer_informatie == "":
            datum = ""
        for rij in lezen:
            if naam_informatie in rij and fietsnummer_informatie in rij:
                datum = rij[2]

fietsnummer_registratie = 0
HoofdMenu()
window.configure(background="yellow")
window.maxsize(300,200)
window.minsize(300,200)
window.mainloop()