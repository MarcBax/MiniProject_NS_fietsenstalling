from  tkinter import *
window = Tk()
window.title("Welkom!")

# auteur: Mark en geholpen door Geert
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

    button_informatie = Button(window, text="informatie ophalen", command=SluitScherm4, bg="blue", fg="white")
    button_informatie.config(height=1, width=15)
    button_informatie.pack(pady=0.1)

    button_quit = Button(window, text='sluiten', command=window.quit, bg='red', fg='white')
    button_quit.config(height=1, width=5)
    button_quit.place(x="258", y="174")

# auteur: Mark en Geert
def RegistreerMenu():
    global w
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

    naam = Label(w, text="Fiets nummer:", fg="black", bg="yellow")
    naam.config(height="1", width="30")
    naam.place(x="0", y="95")

    buttongadoor = Button(w, text="Registreer Gegevens",fg="white", bg="blue")
    buttongadoor.config(height="1", width="15")
    buttongadoor.place(x="185", y="174")

    buttongaterug = Button(w, text="Ga terug",command=OpenHoofdMenu, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    w.configure(background="yellow")
    w.maxsize(300, 200)
    w.minsize(300, 200)

# auteur: Mark
def StalMenu():
    global win
    win = Tk()
    win.title("Stal!")
    label = Label(win, text="Fiets stallen", fg="white", bg="blue")
    label.config(height="1", width="50")
    label.pack()

    naam = Label(win, text="Naam:", fg="white", bg="blue")
    naam.config(height="1", width="12")
    naam.place(x="43", y="65")
    e = Entry(win)
    e.place(x="138", y="66")

    fietsNummer = Label(win, text="Fiets nummer:", fg="white", bg="blue")
    fietsNummer.config(height="1", width="12")
    fietsNummer.place(x="43", y="85")
    e = Entry(win)
    e.place(x="138", y="86")

    buttongadoor = Button(win, text="Stal Fiets", fg="white", bg="blue")
    buttongadoor.config(height="1", width="15")
    buttongadoor.place(x="185", y="174")

    buttongaterug = Button(win, text="Ga terug",command=OpenHoofdMenu1, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    win.configure(background="yellow")
    win.maxsize(300, 200)
    win.minsize(300, 200)

# auteur: Mark
def OphaalMenu():
    global wind
    wind = Tk()
    wind.title("Ophalen!")
    label = Label(wind, text="Fiets ophalen", fg="white", bg="blue")
    label.config(height="1", width="50")
    label.pack()

    buttongadoor = Button(wind, text="haal op", fg="white", bg="blue")
    buttongadoor.config(height="1", width="15")
    buttongadoor.place(x="185", y="174")

    buttongaterug = Button(wind, text="Ga terug",command=OpenHoofdMenu2, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    wind.configure(background="yellow")
    wind.maxsize(300, 200)
    wind.minsize(300, 200)

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

    buttongadoor = Button(windo, text="persoonlijke informatie", fg="white", bg="blue")
    buttongadoor.config(height="1", width="18")
    buttongadoor.place(x="169", y="174")

    buttongaterug = Button(windo, text="Ga terug",command=OpenHoofdMenu3, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    windo.configure(background="yellow")
    windo.maxsize(300, 200)
    windo.minsize(300, 200)

# auteur: Mark
def SluitScherm1():
    window.withdraw()
    RegistreerMenu()

# auteur: Mark
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

# auteur: Mark
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

HoofdMenu()
window.configure(background="yellow")
window.maxsize(300,200)
window.minsize(300,200)
window.mainloop()
