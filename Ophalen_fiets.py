def fiets_ophalen():
    lijst_gestalde_fietsen = []  # lijst maken voor controle naam en nummer
    lijst_opgehaald_fietsen = []  # lijst maken voor nacontrole
    vandaag = datetime.datetime.today()
    datum_tijd = vandaag.strftime("%a %x %X")
    with open('stallen.csv', 'r') as stallencsv:  # naar lijst schrijven
        regels = stallencsv.readlines()
        for line in regels:
            lijst_gestalde_fietsen.append(line)
        naam = input("wat is uw naam? ")
        nummer = input("wat is uw nummer? ")
        tellertje = 0
        for item in lijst_gestalde_fietsen:  # door lijst heen loopen om gebruiker te vinden


            if nummer in item and naam in item:  # gebruiker in lijst zorgt voor een positief getal
                tellertje += 1
        if tellertje > 0:
            lijst_opgehaald_fietsen.append(
                nummer + ";" + naam + ";" + datum_tijd)  # bij een positief getal mag fiets opgehaald worden
            # en wordt de gebruiker in een lijst van ophehaalde fietsen gestopt
            print("u mag uw fiets ophalen.")

        else:  # bij een gebrek aan positief getal krijgt gebruiker een foutmelding
            if tellertje < 1:
                print("onjuiste combinatie")
    print(lijst_gestalde_fietsen)
    print(lijst_opgehaald_fietsen)
