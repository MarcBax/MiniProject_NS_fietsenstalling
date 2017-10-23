import os
import sys
import datetime
import csv

def registreren():                                                          #functie voor het registreren van een fiets
    with open('registratie.csv', 'a') as registrerencsv:
        schrijven = csv.writer(registrerencsv, delimiter = ';')
        while True:
            fietsnummer_registratie = input("Wat is het fietsnummer? ")
            if fietsnummer_registratie == "":                               #als de input ""(niks) is stoppen met while-loop
                break
            naam_registratie = input("Wat is uw naam? ")
            #nog controleren of het fietsnummer of naam al geregistreerd is
            schrijven.writerow((fietsnummer_registratie, naam_registratie)) #rij schrijven van de inputs

def stallen():                                                              #functie voor het stallen van een fiets
    with open('registratie.csv', 'r') as registratiecsv:
        lezen = csv.reader(registratiecsv, delimiter = ';')
        while True:
            fietsnummer_stallen = input("Wat is het fietsnummer? ")
            if fietsnummer_stallen == "":                                   #als de input ""(niks) is stoppen met while-loop
                break
            naam_stallen = input("Wat is uw naam? ")
            combinatie_fietsnummer_naam = fietsnummer_stallen + ';' + naam_stallen
            regels = registratiecsv.readlines()                             #iedere regel van registratie.csv lezen en in een lijst zetten
            teller = 0
            for regel in regels:                                            #iedere regel in de lijst van regels doorlezen
                if combinatie_fietsnummer_naam in regel:                    #als de combinatie van het fietsnummer en naam in de regel staat, bij de teller 1 optellen
                    teller += 1
                    registratie_fietsnummer_naam = combinatie_fietsnummer_naam  #en een variable maken
                else:                                                       #als de combinatie van het fietsnummer en naam niet in de regel staat, bij de teller 0 optellen
                    teller += 0
            if teller == 1:                                                 #als de teller 1 is, dus als het fietsnummer en naam in de registratie csv-file staat
                print("Uw fiets wordt gestald.")
                break
    with open('stallen.csv', 'a') as stallencsv:
        vandaag = datetime.datetime.today()
        datum_tijd = vandaag.strftime("%a %x %X")
        schrijven = csv.writer(stallencsv, delimiter = ';')
        schrijven.writerow((registratie_fietsnummer_naam,datum_tijd))


#def ophalen():

#def informatie_opvragen():


#registreren()
stallen()