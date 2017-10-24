from  tkinter import *
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

    buttongadoor = Button(w, text="Registreer Gegevens", fg="white", bg="blue")
    buttongadoor.config(height="1", width="15")
    buttongadoor.place(x="185", y="174")

    buttongaterug = Button(w, text="Ga terug",command=OpenHoofdMenu, fg="white", bg="red")
    buttongaterug.config(height="1", width="15")
    buttongaterug.place(x="0", y="174")

    w.configure(background="yellow")
    w.maxsize(300, 200)
    w.minsize(300, 200)

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

HoofdMenu()
window.configure(background="yellow")
window.maxsize(300,200)
window.minsize(300,200)
window.mainloop()
