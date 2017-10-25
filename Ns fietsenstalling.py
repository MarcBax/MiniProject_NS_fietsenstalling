from  tkinter import *
from PIL import ImageTk, Image
from captcha.image import ImageCaptcha
import csv
import datetime
import ctypes
import sys
import random
import string
window = Tk()
window.title("Welkom!")


def HoofdMenu():
    label = Label(window, text="Welkom bij de NS-fietsenstalling!", font=("Myriad pro cond",20), bg="blue", fg="white")
    label.config(height=2, width=250)
    label.pack(pady=22)

    button_registreren = Button(window, text="fiets registreren", font=("Myriad pro cond",20), command=SluitScherm1, bg="blue", fg="white")
    button_registreren.config(height=1, width=30)
    button_registreren.pack(pady=1)

    button_stallen = Button(window, text="fiets stallen", font=("Myriad pro cond",20), command=SluitScherm2, bg="blue", fg="white")
    button_stallen.config(height=1, width=30)
    button_stallen.pack(pady=1)

    button_ophalenFiets = Button(window, text="fiets ophalen", font=("Myriad pro cond",20), command=SluitScherm3,bg="blue", fg="white")
    button_ophalenFiets.config(height=1, width=30)
    button_ophalenFiets.pack(pady=1)

    button_informatie = Button(window, text="informatie ophalen", font=("Myriad pro cond",20), command=SluitScherm4,bg="blue", fg="white")
    button_informatie.config(height=1, width=30)
    button_informatie.pack(pady=1)

    button_quit = Button(window, text='sluiten', font=("Myriad pro cond",20), command=window.quit, bg='red', fg='white')
    button_quit.config(height=1, width=5)
    button_quit.place(x="1435", y="730")

def RegistreerMenu():
    global w, e, fietsnummer_registratie
    w = Tk()
    w.title("Registreren!")
    label = Label(w, text="Fiets Registreren", font=("Myriad pro cond",20), fg="white", bg="blue")
    label.config(height="2", width="250")
    label.pack()

    naam = Label(w, text="Naam:", font=("Myriad pro cond",20), fg="white", bg="blue")
    naam.config(height="1", width="30")
    naam.place(x="73", y="255")
    e = Entry(w,width=50)
    e.place(x="600", y="255")

    ctypes.windll.user32.MessageBoxW(0,
                                     "Maak een account aan op telegram en stuur een bericht naar fietsenstallingNS om een tracking ID aan te vragen, als u niet van deze functie gebruik wilt maken voer een 0 in",
                                     "Optionele Telegram notificatie", 1)
    naam = Label(w, text="Telegram ID:", font=("Myriad pro cond",20), fg="white", bg="blue")
    naam.config(height="1", width="30")
    naam.place(x="73", y="300")
    e7 = Entry (w,width=50)
    e7.place(x="600", y="300")


    if fietsnummer_registratie < 99:
        fietsnummer_registratie += 1
        print_text = 'Uw fietsnummer is: ' + str(fietsnummer_registratie)
    else:
        print_text = "Het maximaal aantal fietsen is gestald."
    naam_2 = Label(w, text= print_text, font=("Myriad pro cond",30), fg="black", bg="yellow")
    naam_2.config(height="1", width="30")
    naam_2.place(x="5", y="350")

    naam_registratie = e.get()
    print("Naam: ", str(naam_registratie))
    buttongadoor = Button(w, text="Registreer Gegevens", font=("Myriad pro cond",20), fg="white", bg="blue", command=Registratie)
    buttongadoor.config(height="1", width="30")
    buttongadoor.place(x="1050", y="730")

    buttongaterug = Button(w, text="Ga terug",command=OpenHoofdMenu, font=("Myriad pro cond",20),  fg="white", bg="red")
    buttongaterug.config(height="1", width="30")
    buttongaterug.place(x="0", y="730")

    w.configure(background="yellow")
    w.geometry("{0}x{1}+0+0".format(w.winfo_screenwidth(), w.winfo_screenheight()))

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
    label = Label(win, text="Fiets stallen", font=("Myriad pro cond",20), fg="white", bg="blue")
    label.config(height="2", width="250")
    label.pack()

    naam = Label(win, text="Naam:", font=("Myriad pro cond",20), fg="white", bg="blue")
    naam.config(height="1", width="30")
    naam.place(x="73", y="255")
    e1 = Entry(win, width=50)
    e1.place(x="600", y="255")

    fietsNummer = Label(win, text="Fiets nummer:", font=("Myriad pro cond",20), fg="white", bg="blue")
    fietsNummer.config(height="1", width="30")
    fietsNummer.place(x="73", y="300")
    e2 = Entry(win, width=50)
    e2.place(x="600", y="300")

    buttongadoor = Button(win, text="Stal Fiets", font=("Myriad pro cond",20), fg="white", bg="blue", command=Stallen)
    buttongadoor.config(height="1", width="30")
    buttongadoor.place(x="1050", y="730")

    buttongaterug = Button(win, text="Ga terug", font=("Myriad pro cond",20), command=OpenHoofdMenu1, fg="white", bg="red")
    buttongaterug.config(height="1", width="30")
    buttongaterug.place(x="0", y="730")

    win.configure(background="yellow")
    win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight()))

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
    global wind, e5, e6, chars, text
    wind = Toplevel()
    wind.title("Ophalen!")
    label = Label(wind, text="Fiets ophalen", font=("Myriad pro cond",20), fg="white", bg="blue")
    label.config(height="2", width="250")
    label.pack()

    naam = Label(wind, text="Naam:", font=("Myriad pro cond",20), fg="white", bg="blue")
    naam.config(height="1", width="30")
    naam.place(x="73", y="255")
    e5 = Entry(wind, width=50)
    e5.place(x="600", y="255")

    fietsNummer = Label(wind, text="Fiets nummer:", font=("Myriad pro cond",20), fg="white", bg="blue")
    fietsNummer.config(height="1", width="30")
    fietsNummer.place(x="73", y="300")
    e6 = Entry(wind, width=50)
    e6.place(x="600", y="300")

    captchatekst = Label(wind, text="Vul hieronder de combinatie van cijfers en letters in uit de afbeelding:",font=("Myriad pro cond", 20), fg="white", bg="blue")
    captchatekst.config(height="1", width="60")
    captchatekst.place(x="73", y="450")

    chars = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
    captcha = ImageCaptcha()
    data = captcha.generate(chars)
    image = Image.open(data)
    img = image.resize((480, 120), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    captchaLabel = Label(wind, image=photo)
    captchaLabel.image = photo
    captchaLabel.place(x=73, y=500)

    text = Text(wind, height=1, width=7, font=("Myriad pro cond", 80))
    text.place(x="600", y="500")

    buttongadoor = Button(wind, text="haal op", font=("Myriad pro cond",20), fg="white", bg="blue", command=controle)
    buttongadoor.config(height="1", width="30")
    buttongadoor.place(x="1050", y="730")

    buttongaterug = Button(wind, text="Ga terug", font=("Myriad pro cond",20), command=OpenHoofdMenu2, fg="white", bg="red")
    buttongaterug.config(height="1", width="30")
    buttongaterug.place(x="0", y="730")

    wind.configure(background="yellow")
    wind.geometry("{0}x{1}+0+0".format(wind.winfo_screenwidth(), wind.winfo_screenheight()))

def beveiliging():
    global chars
    chars = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
    captcha = ImageCaptcha()
    data = captcha.generate(chars)
    image = Image.open(data)
    img = image.resize((480, 120), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    captchaLabel = Label(wind, image=photo)
    captchaLabel.image = photo
    captchaLabel.place(x=73, y=500)


def ZekerWeten():
    label = Button(wind, text="Mijn gegevens zijn juist", font=("Myriad pro cond", 20), fg="white", bg="blue", command=controle)
    label.config(height="1", width="30")
    label.place(x=1050, y=730)
    wind.configure(background="yellow")
    wind.geometry("{0}x{1}+0+0".format(wind.winfo_screenwidth(), wind.winfo_screenheight()))


def controle():
    ingevoerd = text.get("1.0", END)
    print(chars)
    print(ingevoerd)
    if ""+ingevoerd.strip() != ""+chars.strip():
        FoutCaptcha()
    else:
        OpenHoofdMenu2()

def FoutCaptcha():
    global window5
    wind.withdraw()
    window5 = Toplevel()
    window5.title("Foute Captcha!")
    label10 = Label(window5, text="De Captcha was onjuist!", bg="blue", fg="white")
    label10.config(height=5, width=70)
    label10.pack(pady=250)
    window5.configure(background="yellow")
    window5.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    gaterug = Button(window5, text="Terug", font=("Myriad pro cond",20), bg="red", fg="white", command=OpenHoofdMenu5)
    gaterug.config(height="1", width="30")
    gaterug.place(x="0", y="730")

def OpenHoofdMenu5():
    window.deiconify()
    window5.withdraw()
    for gegevens in window5.winfo_children():
        gegevens.destroy()

def Ophalen():
    schrijven_ophalen()
    OpenHoofdMenu2()

def schrijven_ophalen():
    global e5, e6
    naam = e5.get()
    fietsnummer = e6.get()
    fiets_ophalen(naam, fietsnummer)

# auteur: Mark
def InfoMenu():
    global windo
    windo = Tk()
    windo.title("Informatie!")
    label = Label(windo, text="Informatie", font=("Myriad pro cond",20), fg="white", bg="blue")
    label.config(height="2", width="250")
    label.pack()
    info = Label(windo, text="Deze fietsen stalling heeft 99 plekken en is 24/7 open.", font=("Myriad pro cond",20), fg="black", bg="yellow")
    info.config(height="2", width="45")
    info.pack()

    with open('stallen.csv') as lezenstallencsv:
        regels = lezenstallencsv.readlines()
        if len(regels) > 1:
            plekken_over = "Er zijn " + str(int(100 - len(regels) / 2)) + " plekken over."
        elif len(regels) == 1:
            plekken_over = "Er zijn 99 plekken over."

    info = Label(windo, text=plekken_over, font=("Myriad pro cond",20), fg="black", bg="yellow")
    info.config(height="2", width="30")
    info.pack()

    buttongadoor = Button(windo, text="persoonlijke informatie", font=("Myriad pro cond",20), fg="white", bg="blue", command=Open_persoonlijke_informatie)
    buttongadoor.config(height="1", width="30")
    buttongadoor.place(x="1050", y="730")

    buttongaterug = Button(windo, text="Ga terug",command=OpenHoofdMenu3, font=("Myriad pro cond",20), fg="white", bg="red")
    buttongaterug.config(height="1", width="30")
    buttongaterug.place(x="0", y="730")

    windo.configure(background="yellow")
    windo.geometry("{0}x{1}+0+0".format(windo.winfo_screenwidth(), windo.winfo_screenheight()))

def Open_persoonlijke_informatie():
    windo.withdraw()
    Persoonlijke_informatie()

def Persoonlijke_informatie():
    global window1, e3, e4
    window1 = Tk()
    window1.title("Informatie!")
    label = Label(windo, text="Informatie", font=("Myriad pro cond",20), fg="white", bg="blue")
    label.config(height="2", width="250")
    label.pack()

    naam = Label(window1, text="Naam:", font=("Myriad pro cond",20), fg="white", bg="blue")
    naam.config(height="1", width="30")
    naam.place(x="73", y="255")
    e3 = Entry(window1, width=50)
    e3.place(x="600", y="255")

    fietsNummer = Label(window1, text="Fiets nummer:", font=("Myriad pro cond",20), fg="white", bg="blue")
    fietsNummer.config(height="1", width="30")
    fietsNummer.place(x="73", y="300")
    e4 = Entry(window1, width=50)
    e4.place(x="600", y="300")

    buttongadoor = Button(window1, text="opvragen", font=("Myriad pro cond",20), fg="white", bg="blue",command=aanroepen_informatie)
    buttongadoor.config(height="1", width="30")
    buttongadoor.place(x="1050", y="730")

    buttongaterug = Button(window1, text="Ga terug", command=OpenHoofdMenu4, font=("Myriad pro cond",20), fg="white", bg="red")
    buttongaterug.config(height="1", width="30")
    buttongaterug.place(x="0", y="730")

    window1.configure(background="yellow")
    window1.configure(background="yellow")
    window1.geometry("{0}x{1}+0+0".format(windo.winfo_screenwidth(), windo.winfo_screenheight()))

def aanroepen_informatie():
    window1.withdraw()
    schrijven_persoonlijke_informatie()
    pop_up_informatie_datum()

def schrijven_persoonlijke_informatie():
    global e3, e4
    naam = e3.get()
    fietsnummer = e4.get()
    informatie_opvragen(naam, fietsnummer)

def pop_up_informatie_datum():
    global datum, window2
    window2 = Tk()
    window2.title("Informatie!")
    label = Label(windo, text="Datum",font=("Myriad pro cond",20), fg="white", bg="blue")
    label.config(height="1", width="50")
    label.place(x=300, y=50)

    naam_3 = Label(window2, text=datum, font=("Myriad pro cond",20), fg="black", bg="yellow")
    naam_3.config(height="3", width="50")
    naam_3.place(x=300, y=100)

    buttongaterug = Button(window2, text="sluiten", font=("Myriad pro cond",20), command=SluitScherm5, fg="white", bg="red")
    buttongaterug.config(height="1", width="30")
    buttongaterug.place(x="0", y="730")

    window2.configure(background="yellow")
    window2.geometry("{0}x{1}+0+0".format(window2.winfo_screenwidth(), window2.winfo_screenheight()))

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

def SluitScherm5():
    window.deiconify()
    window2.withdraw()


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

#auteur: Marc Bax
def fiets_ophalen(naam_ophalen, fietsnummer_ophalen):
    infile = open('stallen.csv', 'r')
    lijst_gestalde_fietsen = infile.readlines()
    lijst_gestalde_fietsen.remove('fietsnummer;naam;datum\n')
    infile.close()
    outfile = open('stallen.csv', 'w')
    outfile.write('fietsnummer;naam;datum\n')
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
    with open('stallen.csv', 'r') as lezenstallencsv:
        lezen = csv.reader(lezenstallencsv, delimiter=';')
        if naam_informatie or fietsnummer_informatie == "":
            datum = ""
        teller = 0
        for rij in lezen:
            if naam_informatie in rij and fietsnummer_informatie in rij:
                teller += 1
                datum_tijd = rij[2]
            else:
                teller += 0
        if teller == 1:
            datum = "Uw fiets is gestald op: " + datum_tijd
        else:
            datum = "Uw fiets is niet meer gestald."

fietsnummer_registratie = 0
HoofdMenu()
window.configure(background="yellow")
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.mainloop()