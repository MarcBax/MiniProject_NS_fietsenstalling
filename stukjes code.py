import datetime

#inputs voor registratie
naam = input("Wat is je naam? ")
fietsnummer = input("Wat is het nummer van de fiets? ")
#datum =

#csv file schrijven
with open('registratie.csv', 'w') as registrerencsv:
    schrijven = registratiecsv.writer(registrerencsv, delimiter = ';')
    schrijven.writerow(('fietsnummer', 'naam', 'datum'))
    #de rest van de code voor het csv file, als de tab weg is wordt het bestand gesloten

#csv file lezen
with open('registratie.csv', 'r') as registratiecsv:
    lezen = csv.reader(registratiecsv, delimiter = ';')
    for rij in lezen:
        #en de rest
    #de rest van de code voor het csv file, als de tab weg is worddt het bestand gesloten

#datum en tijd invoeren
vandaag = datetime.datetime.today()
datum_tijd = vandaag.strftime("%a %x; %X")
print(datum_tijd)
