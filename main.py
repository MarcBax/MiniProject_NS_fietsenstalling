import os
import sys
import datetime
import csv

def registreren():                                                          #functie voor het registreren van een fiets
    while True:
        fietsnummer_registratie = input("Wat is het fietsnummer? ")
        if fietsnummer_registratie == "":                                   # als de input ""(niks) is stoppen met while-loop
            break
        naam_registratie = input("Wat is uw naam? ")
        with open('registratie.csv', 'r') as lezenregistrerencsv:
                regels = lezenregistrerencsv.readlines()                    #iedere regel van registratie.csv lezen en in een lijst zetten
                teller_fietsnummer = 0
                teller_naam = 0
                for regel in regels:                                            #iedere regel in de lijst van regels doorlezen
                    if fietsnummer_registratie in regel:                        #als het fietsnummer in de regel staat, bij de teller van het fietsnummer 1 optellen
                        teller_fietsnummer += 1
                    else:                                                       #als het fietsnummer niet in de regel staat, bij de teller van het fietsnummer 0 optellen
                        teller_fietsnummer += 0
                    if naam_registratie in regel:                               #als de naam in de regel staat, bij de teller van de naam 1 optellen
                        teller_naam += 1
                    else:                                                       #als de naam niet in de regel staat, bij de teller van de naam 1 optellen
                        teller_naam += 0
                if teller_fietsnummer == 1:                                     #als de teller van het fietsnummer 1 is, dus als het fietsnummer in de registratie csv-file staat
                    print("Uw fietsnummer is al geregistreerd.")
                    continue
                if teller_naam == 1:                                            #als de teller van de naam 1 is, dus als de naam in de registratie csv-file staat
                    print("Uw naam is al geregistreerd.")
                    continue
        with open('registratie.csv', 'a') as registrerencsv:
            schrijven = csv.writer(registrerencsv, delimiter = ';')
            schrijven.writerow((fietsnummer_registratie, naam_registratie))     #rij schrijven van de inpu

def stallen():                                                                  #functie voor het stallen van een fiets
    while True:
        fietsnummer_stallen = input("Wat is het fietsnummer? ")
        if fietsnummer_stallen == "":                                           # als de input ""(niks) is stoppen met while-loop
            break
        naam_stallen = input("Wat is uw naam? ")
        with open('registratie.csv', 'r') as registratiecsv:
            #lezen = csv.reader(registratiecsv, delimiter = ';')
            regels = registratiecsv.readlines()                             #iedere regel van registratie.csv lezen en in een lijst zetten
            teller = 0
            for regel in regels:                                            #iedere regel in de lijst van regels doorlezen
                if fietsnummer_stallen in regel and naam_stallen in regel:  #als de combinatie van het fietsnummer en naam in de regel staat, bij de teller 1 optellen
                    teller += 1
                    registratie_fietsnummer = fietsnummer_stallen           #een variable maken
                    registratie_naam = naam_stallen
                else:                                                       #als de combinatie van het fietsnummer en naam niet in de regel staat, bij de teller 0 optellen
                    teller += 0
            if teller == 0:
                print("Uw fietsnummer in combinatie met uw naam is nog niet geregistreerd, probeer het opnieuw.")
                stallen()
            elif teller == 1:                                                #als de teller 1 is, dus als het fietsnummer en naam in de registratie csv-file staat
                with open('stallen.csv', 'r') as lezenstallencsv:
                    controle_regel = lezenstallencsv.readlines()            #iedere regel van het bestand stallen.csv in een lijst zetten
                    teller = 0
                    for regel in controle_regel:                            #voor iedere regel in de lijst met regels
                        if fietsnummer_stallen in regel and naam_stallen in regel:  #als het fietsnummer en de naam in de regel staat
                            teller += 1
                        else:                                                       #als het fietsnummer en de naam niet in de regel staat
                            teller += 0
                    if teller == 1:                                         #als de teller 1 is
                        print("Uw fietsnummer in combinatie met uw naam is al gestald, probeer het opnieuw.")
                        stallen()
                    else:                                                   #als de teller niet 0 is
                        print("Uw fiets wordt gestald.")
        with open('stallen.csv', 'a') as stallencsv:
            vandaag = datetime.datetime.today()
            datum_tijd = vandaag.strftime("%a %x %X")                           #de huidige datum en tijd
            schrijven = csv.writer(stallencsv, delimiter = ';')
            schrijven.writerow((registratie_fietsnummer, registratie_naam, datum_tijd))       #in stallen.csv de variable schrijven

#def ophalen():

#def informatie_opvragen():

registreren()
stallen()