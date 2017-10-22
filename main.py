import os
import sys
import datetime
import csv

def registreren():                                                          #functie voor het registreren van een fiets
    with open('registratie.csv', 'w') as registrerencsv:
        schrijven = csv.writer(registrerencsv, delimiter = ';')
        schrijven.writerow(('fietsnummer', 'naam'))                         #titel schrijven in csv file
        while True:
            fietsnummer_registratie = input("Wat is het fietsnummer? ")
            if fietsnummer_registratie == "":                               #als de input ""(niks) is stoppen met while-loop
                break
            naam_registratie = input("Wat is uw naam? ")
            schrijven.writerow((fietsnummer_registratie, naam_registratie)) #rij schrijven van de inputs

def stallen():                                                              #functie voor het stallen van een fiets
    with open('registratie.csv', 'r') as registratiecsv:
        lezen = csv.reader(registratiecsv, delimiter = ';')
        registratie_set = {}
        while True:
            fietsnummer_stallen = input("Wat is het fietsnummer? ")
            if fietsnummer_stallen == "":                                   #als de input ""(niks) is stoppen met while-loop
                break
            naam_stallen = input("Wat is uw naam? ")



#def ophalen():


#def informatie_opvragen():

#test
#registreren()
#stallen()