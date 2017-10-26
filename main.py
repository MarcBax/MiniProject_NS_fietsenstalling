from  tkinter import *
from PIL import ImageTk, Image
from captcha.image import ImageCaptcha
import requests
import csv
import datetime
import sys
import random
import string
Scherm_HoofdMenu = Tk()
Scherm_HoofdMenu.title("Welkom!")

# auteur: Mark Gasse
# Laat het scherm hoofd menu zien als je het programma opstart en zorgt dat je verbinding maakt met andere schermen
def HoofdMenu():
    label_hoofd_menu = Label(Scherm_HoofdMenu, text="Welkom bij de NS-fietsenstalling!", font=("Myriad pro cond",20), bg="blue", fg="white")
    label_hoofd_menu.config(height=2, width=250)
    label_hoofd_menu.pack(pady=22)

    knop_registreren = Button(Scherm_HoofdMenu, text="fiets registreren", font=("Myriad pro cond",20), command=SluitScherm1, bg="blue", fg="white")
    knop_registreren.config(height=1, width=30)
    knop_registreren.pack(pady=1)

    knop_stallen = Button(Scherm_HoofdMenu, text="fiets stallen", font=("Myriad pro cond",20), command=SluitScherm2, bg="blue", fg="white")
    knop_stallen.config(height=1, width=30)
    knop_stallen.pack(pady=1)

    knop_ophalenFiets = Button(Scherm_HoofdMenu, text="fiets ophalen", font=("Myriad pro cond",20), command=SluitScherm3,bg="blue", fg="white")
    knop_ophalenFiets.config(height=1, width=30)
    knop_ophalenFiets.pack(pady=1)

    knop_informatie = Button(Scherm_HoofdMenu, text="informatie ophalen", font=("Myriad pro cond",20), command=SluitScherm4,bg="blue", fg="white")
    knop_informatie.config(height=1, width=30)
    knop_informatie.pack(pady=1)

    knop_quit = Button(Scherm_HoofdMenu, text='sluiten', font=("Myriad pro cond",20), command=Scherm_HoofdMenu.quit, bg='red', fg='white')
    knop_quit.config(height=1, width=5)
    knop_quit.place(x="1435", y="630")

# auteur: Mark Gasse
# Laat het scherm zien van registreren en maakt verbinding met andere functies
def RegistreerMenu():
    global Scherm_Registratie, naam_registreer, telegram, fietsnummer_registratie, tele_registratie
    Scherm_Registratie = Tk()
    Scherm_Registratie.title("Registreren!")
    label_registratie = Label(Scherm_Registratie, text="Fiets Registreren", font=("Myriad pro cond",20), fg="white", bg="blue")
    label_registratie.config(height="2", width="250")
    label_registratie.pack()

    naam_registreer = Label(Scherm_Registratie, text="Naam:", font=("Myriad pro cond",20), fg="white", bg="blue")
    naam_registreer.config(height="1", width="30")
    naam_registreer.place(x="73", y="255")
    naam_registreer = Entry(Scherm_Registratie,width=50)
    naam_registreer.place(x="600", y="255")

#"Maak een account aan op telegram en stuur een bericht naar fietsenstallingNS om een tracking ID aan te vragen, als u niet van deze functie gebruik wilt maken voer niets in"

    naam_telegram = Label(Scherm_Registratie, text="Telegram ID:", font=("Myriad pro cond",20), fg="white", bg="blue")
    naam_telegram.config(height="1", width="30")
    naam_telegram.place(x="73", y="300")
    telegram = Entry (Scherm_Registratie,width=50)
    telegram.place(x="600", y="300")

    if fietsnummer_registratie < 99:
        fietsnummer_registratie += 1
        print_fietsnummertext = 'Uw fietsnummer is: ' + str(fietsnummer_registratie) +"\n"
    else:
        print_fietsnummertext = "Het maximaal aantal fietsen is gestald.\n"

    Beschikbare_plaatsen = Label(Scherm_Registratie, text= print_fietsnummertext, font=("Myriad pro cond",30), fg="black", bg="yellow")
    Beschikbare_plaatsen.config(height="2", width="30")
    Beschikbare_plaatsen.place(x="5", y="400")

    print_telegramtext = "Optioneel\n" \
                         "Maak een account aan op telegram en stuur een bericht naar fietsenstallingNS om een tracking ID aan te vragen, \n" \
                         "als u niet van deze functie gebruik wilt maken voer niets in"

    telegramid_info = Label(Scherm_Registratie, text=print_telegramtext, font=("Myriad pro cond", 15), fg="black",bg="yellow")
    telegramid_info.config(height="3", width="100")
    telegramid_info.place(x="5", y="100")

    tele_registratie = telegram.get()

    knopGaDoor = Button(Scherm_Registratie, text="Registreer Gegevens", font=("Myriad pro cond",20), fg="white", bg="blue", command=Registratie)
    knopGaDoor.config(height="1", width="30")
    knopGaDoor.place(x="1050", y="630")

    knopGaTerug = Button(Scherm_Registratie, text="Ga terug",command=OpenHoofdMenu, font=("Myriad pro cond",20),  fg="white", bg="red")
    knopGaTerug.config(height="1", width="30")
    knopGaTerug.place(x="0", y="630")

    Scherm_Registratie.configure(background="yellow")
    Scherm_Registratie.geometry("{0}x{1}+0+0".format(Scherm_Registratie.winfo_screenwidth(), Scherm_Registratie.winfo_screenheight()))

def Registratie():
    schrijven_registreren()
    OpenHoofdMenu()

def schrijven_registreren():
    global naam_registreer, telegram, teleID
    naam = naam_registreer.get()
    teleID = telegram.get()
    registreren(naam, teleID)


def StalMenu():
    global Scherm_stal, stal_naam, Stal_fiets_nummer
    Scherm_stal = Tk()
    Scherm_stal.title("Stal!")
    label_stallen = Label(Scherm_stal, text="Fiets stallen", font=("Myriad pro cond",20), fg="white", bg="blue")
    label_stallen.config(height="2", width="250")
    label_stallen.pack()

    naam_stallen = Label(Scherm_stal, text="Naam:", font=("Myriad pro cond",20), fg="white", bg="blue")
    naam_stallen.config(height="1", width="30")
    naam_stallen.place(x="73", y="255")
    stal_naam = Entry(Scherm_stal, width=50)
    stal_naam.place(x="600", y="255")

    fietsNummer = Label(Scherm_stal, text="Fiets nummer:", font=("Myriad pro cond",20), fg="white", bg="blue")
    fietsNummer.config(height="1", width="30")
    fietsNummer.place(x="73", y="300")
    Stal_fiets_nummer = Entry(Scherm_stal, width=50)
    Stal_fiets_nummer.place(x="600", y="300")

    knopGaDoor = Button(Scherm_stal, text="Stal Fiets", font=("Myriad pro cond",20), fg="white", bg="blue", command=Stallen)
    knopGaDoor.config(height="1", width="30")
    knopGaDoor.place(x="1050", y="630")

    knopGaTerug = Button(Scherm_stal, text="Ga terug", font=("Myriad pro cond",20), command=OpenHoofdMenu1, fg="white", bg="red")
    knopGaTerug.config(height="1", width="30")
    knopGaTerug.place(x="0", y="630")

    Scherm_stal.configure(background="yellow")
    Scherm_stal.geometry("{0}x{1}+0+0".format(Scherm_stal.winfo_screenwidth(), Scherm_stal.winfo_screenheight()))

def Stallen():
    schrijven_stallen()
    OpenHoofdMenu1()

def schrijven_stallen():
    global stal_naam, Stal_fiets_nummer, telegram
    with open('registratie.csv', 'r') as lezenstallencsv:
        lezen = csv.reader(lezenstallencsv, delimiter=';')
        for rij in lezen:
            if Stal_fiets_nummer.get() in rij and stal_naam.get() in rij:
                teleID = rij[2]
                naam = rij[1]
                fietsnummer = rij[0]
                stallen(naam, fietsnummer, teleID)

# auteur: Mark
def OphaalMenu():
    global Scherm_Haal_Op, naam_ophalen, fiets_nummer, chars, text
    Scherm_Haal_Op = Toplevel()
    Scherm_Haal_Op.title("Ophalen!")
    label_ophalen = Label(Scherm_Haal_Op, text="Fiets ophalen", font=("Myriad pro cond",20), fg="white", bg="blue")
    label_ophalen.config(height="2", width="250")
    label_ophalen.pack()

    naamOphalen = Label(Scherm_Haal_Op, text="Naam:", font=("Myriad pro cond",20), fg="white", bg="blue")
    naamOphalen.config(height="1", width="30")
    naamOphalen.place(x="73", y="255")
    naam_ophalen = Entry(Scherm_Haal_Op, width=50)
    naam_ophalen.place(x="600", y="255")

    fietsNummer = Label(Scherm_Haal_Op, text="Fiets nummer:", font=("Myriad pro cond",20), fg="white", bg="blue")
    fietsNummer.config(height="1", width="30")
    fietsNummer.place(x="73", y="300")
    fiets_nummer = Entry(Scherm_Haal_Op, width=50)
    fiets_nummer.place(x="600", y="300")

    captchatekst = Label(Scherm_Haal_Op, text="Vul hieronder de combinatie van cijfers en letters in uit de afbeelding:",font=("Myriad pro cond", 20), fg="white", bg="blue")
    captchatekst.config(height="1", width="60")
    captchatekst.place(x="73", y="450")

    chars = ''.join([random.choice(string.ascii_letters.upper() + string.digits) for n in range(5)])
    captcha = ImageCaptcha()
    data = captcha.generate(chars)
    image = Image.open(data)
    img = image.resize((480, 120), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    captchaLabel = Label(Scherm_Haal_Op, image=photo)
    captchaLabel.image = photo
    captchaLabel.place(x=73, y=500)

    text = Text(Scherm_Haal_Op, height=1, width=7, font=("Myriad pro cond", 80))
    text.place(x="600", y="500")

    knopGaDoor = Button(Scherm_Haal_Op, text="haal op", font=("Myriad pro cond",20), fg="white", bg="blue", command=controle)
    knopGaDoor.config(height="1", width="30")
    knopGaDoor.place(x="1050", y="630")

    knopGaTerug = Button(Scherm_Haal_Op, text="Ga terug", font=("Myriad pro cond",20), command=OpenHoofdMenu2, fg="white", bg="red")
    knopGaTerug.config(height="1", width="30")
    knopGaTerug.place(x="0", y="630")

    Scherm_Haal_Op.configure(background="yellow")
    Scherm_Haal_Op.geometry("{0}x{1}+0+0".format(Scherm_Haal_Op.winfo_screenwidth(), Scherm_Haal_Op.winfo_screenheight()))

def beveiliging():
    global chars
    chars = ''.join([random.choice(string.ascii_letters.upper() + string.digits) for n in range(5)])
    captcha = ImageCaptcha()
    data = captcha.generate(chars)
    image = Image.open(data)
    img = image.resize((480, 120), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    captchaLabel = Label(Scherm_Haal_Op, image=photo)
    captchaLabel.image = photo
    captchaLabel.place(x=73, y=500)


def ZekerWeten():
    label_gegevens = Button(Scherm_Haal_Op, text="Mijn gegevens zijn juist", font=("Myriad pro cond", 20), fg="white", bg="blue", command=controle)
    label_gegevens.config(height="1", width="30")
    label_gegevens.place(x=1050, y=630)
    Scherm_Haal_Op.configure(background="yellow")
    Scherm_Haal_Op.geometry("{0}x{1}+0+0".format(Scherm_Haal_Op.winfo_screenwidth(), Scherm_Haal_Op.winfo_screenheight()))


def controle():
    ingevoerd = text.get("1.0", END)
    ingevoerd = ingevoerd.upper()
    if ""+ingevoerd.strip() != ""+chars.strip():
        FoutCaptcha()
    else:
        Ophalen()

def FoutCaptcha():
    global Scherm_Captcha
    Scherm_Haal_Op.withdraw()
    Scherm_Captcha = Toplevel()
    Scherm_Captcha.title("Foute Captcha!")
    labelCaptcha = Label(Scherm_Captcha, text="De Captcha was onjuist!", bg="blue", fg="white")
    labelCaptcha.config(height=5, width=70)
    labelCaptcha.pack(pady=250)
    Scherm_Captcha.configure(background="yellow")
    Scherm_Captcha.geometry("{0}x{1}+0+0".format(Scherm_HoofdMenu.winfo_screenwidth(), Scherm_HoofdMenu.winfo_screenheight()))
    GaTerug = Button(Scherm_Captcha, text="Terug", font=("Myriad pro cond",20), bg="red", fg="white", command=OpenHoofdMenu5)
    GaTerug.config(height="1", width="30")
    GaTerug.place(x="0", y="630")

def OpenHoofdMenu5():
    Scherm_HoofdMenu.deiconify()
    Scherm_Captcha.withdraw()
    for gegevens in Scherm_Captcha.winfo_children():
        gegevens.destroy()

def Ophalen():
    schrijven_ophalen()
    OpenHoofdMenu2()

def schrijven_ophalen():
    global naam_ophalen, fiets_nummer
    naam = naam_ophalen.get()
    fietsnummer = fiets_nummer.get()
    fiets_ophalen(naam, fietsnummer)

# auteur: Mark
def InfoMenu():
    global Scherm_info
    Scherm_info = Tk()
    Scherm_info.title("Informatie!")
    label_info = Label(Scherm_info, text="Informatie", font=("Myriad pro cond",20), fg="white", bg="blue")
    label_info.config(height="2", width="250")
    label_info.pack()
    info = Label(Scherm_info, text="Deze fietsen stalling heeft 99 plekken en is 24/7 open.", font=("Myriad pro cond",20), fg="black", bg="yellow")
    info.config(height="2", width="45")
    info.pack()

    with open('stallen.csv') as lezenstallencsv:
        regels = lezenstallencsv.readlines()
        if len(regels) > 1:
            plekken_over = "Er zijn " + str(int(100 - len(regels) / 2)) + " plekken over."
        elif len(regels) == 1:
            plekken_over = "Er zijn 99 plekken over."

    info = Label(Scherm_info, text=plekken_over, font=("Myriad pro cond",20), fg="black", bg="yellow")
    info.config(height="2", width="30")
    info.pack()

    knopGaDoor = Button(Scherm_info, text="persoonlijke informatie", font=("Myriad pro cond",20), fg="white", bg="blue", command=Open_persoonlijke_informatie)
    knopGaDoor.config(height="1", width="30")
    knopGaDoor.place(x="1050", y="630")

    knopGaTerug = Button(Scherm_info, text="Ga terug",command=OpenHoofdMenu3, font=("Myriad pro cond",20), fg="white", bg="red")
    knopGaTerug.config(height="1", width="30")
    knopGaTerug.place(x="0", y="630")

    Scherm_info.configure(background="yellow")
    Scherm_info.geometry("{0}x{1}+0+0".format(Scherm_info.winfo_screenwidth(), Scherm_info.winfo_screenheight()))

def Open_persoonlijke_informatie():
    Scherm_info.withdraw()
    Persoonlijke_informatie()

def Persoonlijke_informatie():
    global Scherm_persoonlijk, persoonlijke_naam, persoonlijk_fietsNummer
    Scherm_persoonlijk = Tk()
    Scherm_persoonlijk.title("Informatie!")
    label_info = Label(Scherm_info, text="Informatie", font=("Myriad pro cond",20), fg="white", bg="blue")
    label_info.config(height="2", width="250")
    label_info.pack()

    naamPersoonlijk = Label(Scherm_persoonlijk, text="Naam:", font=("Myriad pro cond",20), fg="white", bg="blue")
    naamPersoonlijk.config(height="1", width="30")
    naamPersoonlijk.place(x="73", y="255")
    persoonlijke_naam = Entry(Scherm_persoonlijk, width=50)
    persoonlijke_naam.place(x="600", y="255")

    fietsNummer = Label(Scherm_persoonlijk, text="Fiets nummer:", font=("Myriad pro cond",20), fg="white", bg="blue")
    fietsNummer.config(height="1", width="30")
    fietsNummer.place(x="73", y="300")
    persoonlijk_fietsNummer = Entry(Scherm_persoonlijk, width=50)
    persoonlijk_fietsNummer.place(x="600", y="300")

    knopGaDoor = Button(Scherm_persoonlijk, text="opvragen", font=("Myriad pro cond",20), fg="white", bg="blue",command=aanroepen_informatie)
    knopGaDoor.config(height="1", width="30")
    knopGaDoor.place(x="1050", y="630")

    knopGaTerug = Button(Scherm_persoonlijk, text="Ga terug", command=OpenHoofdMenu4, font=("Myriad pro cond",20), fg="white", bg="red")
    knopGaTerug.config(height="1", width="30")
    knopGaTerug.place(x="0", y="630")

    Scherm_persoonlijk.configure(background="yellow")
    Scherm_persoonlijk.configure(background="yellow")
    Scherm_persoonlijk.geometry("{0}x{1}+0+0".format(Scherm_info.winfo_screenwidth(), Scherm_info.winfo_screenheight()))

def aanroepen_informatie():
    Scherm_persoonlijk.withdraw()
    schrijven_persoonlijke_informatie()
    pop_up_informatie()

def schrijven_persoonlijke_informatie():
    global persoonlijke_naam, persoonlijk_fietsNummer
    naam = persoonlijke_naam.get()
    fietsnummer = persoonlijk_fietsNummer.get()
    informatie_opvragen(naam, fietsnummer)

def pop_up_informatie():
    global datum, Scherm_info_pop, telegramIDshow
    Scherm_info_pop = Tk()
    Scherm_info_pop.title("Informatie!")
    labelDatum = Label(Scherm_info, text="Datum",font=("Myriad pro cond",20), fg="white", bg="blue")
    labelDatum.config(height="1", width="50")
    labelDatum.place(x=300, y=50)

    datumPopUp = Label(Scherm_info_pop, text=datum, font=("Myriad pro cond",20), fg="black", bg="yellow")
    datumPopUp.config(height="3", width="50")
    datumPopUp.place(x=300, y=100)

    telegram_3 = Label(Scherm_info_pop, text=telegramIDshow, font=("Myriad pro cond",20), fg="black", bg="yellow")
    telegram_3.config(height="3", width="50")
    telegram_3.place(x=300, y=200)

    knopGaTerug = Button(Scherm_info_pop, text="sluiten", font=("Myriad pro cond",20), command=SluitScherm5, fg="white", bg="red")
    knopGaTerug.config(height="1", width="30")
    knopGaTerug.place(x="0", y="630")

    Scherm_info_pop.configure(background="yellow")
    Scherm_info_pop.geometry("{0}x{1}+0+0".format(Scherm_info_pop.winfo_screenwidth(), Scherm_info_pop.winfo_screenheight()))

#auteur: Mark
def SluitScherm1():
    Scherm_HoofdMenu.withdraw()
    RegistreerMenu()

#auteur: Mark
def SluitScherm2():
    Scherm_HoofdMenu.withdraw()
    StalMenu()

# auteur: Mark
def SluitScherm3():
    Scherm_HoofdMenu.withdraw()
    OphaalMenu()

# auteur: Mark
def SluitScherm4():
    Scherm_HoofdMenu.withdraw()
    InfoMenu()

def SluitScherm5():
    Scherm_HoofdMenu.deiconify()
    Scherm_info_pop.withdraw()


def OpenHoofdMenu():
    Scherm_HoofdMenu.deiconify()
    Scherm_Registratie.withdraw()
    for gegevens in Scherm_Registratie.winfo_children():
        gegevens.destroy()

# auteur: Mark
def OpenHoofdMenu1():
    Scherm_HoofdMenu.deiconify()
    Scherm_stal.withdraw()
    for gegevens in Scherm_stal.winfo_children():
        gegevens.destroy()

# auteur: Mark
def OpenHoofdMenu2():
    Scherm_HoofdMenu.deiconify()
    Scherm_Haal_Op.withdraw()
    for gegevens in Scherm_Haal_Op.winfo_children():
        gegevens.destroy()

# auteur: Mark
def OpenHoofdMenu3():
    Scherm_HoofdMenu.deiconify()
    Scherm_info.withdraw()
    for gegevens in Scherm_info.winfo_children():
        gegevens.destroy()

def OpenHoofdMenu4():
    Scherm_HoofdMenu.deiconify()
    Scherm_persoonlijk.withdraw()
    for gegevens in Scherm_persoonlijk.winfo_children():
        gegevens.destroy()

#auteur: Marc Bax
def registreren(naam_registratie,teleID_registratie ):              #functie voor het registreren van een fiets
    global fietsnummer_registratie

    with open('registratie.csv', 'a') as registrerencsv:
        schrijven = csv.writer(registrerencsv, delimiter = ';')
        schrijven.writerow((fietsnummer_registratie, naam_registratie, teleID_registratie))     #rij schrijven van de inputs

#auteur: Marc Bax
def stallen(naam_stallen, fietsnummer_stallen, teleID_stallen):                           #functie voor het stallen van een fiets
    global datum_tijd
    with open('stallen.csv', 'a') as stallencsv:
        vandaag = datetime.datetime.today()
        datum_tijd = vandaag.strftime("%a %x %X")                           #de huidige datum en tijd
        schrijven = csv.writer(stallencsv, delimiter = ';')
        schrijven.writerow((fietsnummer_stallen, naam_stallen, teleID_stallen, datum_tijd))       #in stallen.csv de variable schrijven

#auteur: Marc Bax
def fiets_ophalen(naam_ophalen, fietsnummer_ophalen):
    with open('stallen.csv', 'r') as lezenstallencsv:
        lezen = csv.reader(lezenstallencsv, delimiter=';')
        for rij in lezen:
            if naam_ophalen in rij and fietsnummer_ophalen in rij:
                TeleID =rij[2]
                if TeleID == "":
                    TeleID = 0
                if int(TeleID) > 9999:
                    nu = datetime.datetime.today()
                    datum_nu = nu.strftime("%a %x %X")
                    telerequest = "https://api.telegram.org/bot458958945:AAENUyVr_1PGmhmL_T4mV356-UzIihx4yrg/SendMessage?chat_id=" + str(
                        TeleID) + "&text=Je fiets is opgehaald op " + datum_nu + "\nUw bij NS geregisteerd fietsnummer is : " + fietsnummer_ophalen + \
                                  "\nUw geregisteerde naam is : " + naam_ophalen +"\nU kunt deze gegevens volgende keer weer gebruiken, prettige dag."
                    requests.get(telerequest)
            else:
                continue

    infile = open('stallen.csv', 'r')
    lijst_gestalde_fietsen = infile.readlines()
    lijst_gestalde_fietsen.remove('fietsnummer;naam;telegramID;datum\n')
    infile.close()
    outfile = open('stallen.csv', 'w')
    outfile.write('fietsnummer;naam;telegramID;datum\n')
    for regel in lijst_gestalde_fietsen:
        partsRegel = regel.rstrip().split(";")
        if len(partsRegel) >= 2:
            if naam_ophalen != partsRegel[1] and fietsnummer_ophalen != partsRegel[0]:
                outfile.write(regel)
                outfile.write('\n')
    outfile.close()

#auteur: Marc Bax
def informatie_opvragen(naam_informatie, fietsnummer_informatie):
    global datum
    global telegramIDshow
    with open('stallen.csv', 'r') as lezenstallencsv:
        lezen = csv.reader(lezenstallencsv, delimiter=';')
        if naam_informatie or fietsnummer_informatie == "":
            datum = ""
            telegramIDshow = ""
        teller = 0
        for rij in lezen:
            if naam_informatie in rij and fietsnummer_informatie in rij:
                teller += 1
                datum_tijd = rij[3]
                Telegram_ID =rij[2]
            else:
                teller += 0

        if teller == 1:
            datum = "Uw fiets is gestald op: " + datum_tijd
            telegramIDshow = "Uw Telegram ID is :" + Telegram_ID
        else:
            datum = "Uw fiets is niet meer gestald."
            telegramIDshow = "Uw Telegram ID is : 0"

fietsnummer_registratie = 0
HoofdMenu()
Scherm_HoofdMenu.configure(background="yellow")
Scherm_HoofdMenu.geometry("{0}x{1}+0+0".format(Scherm_HoofdMenu.winfo_screenwidth(), Scherm_HoofdMenu.winfo_screenheight()))
Scherm_HoofdMenu.mainloop()