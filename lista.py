import sys

#poprawianie
org_lista = open('lista.txt', encoding='utf-8').readlines()
licznik = 1
k = 0
lista = [] #lista do użytku w generowaniu plików txt
nowalista = open('lista_updated.txt', 'w', encoding='utf8') #lista referyncyjna txt
for l in range(len(org_lista)):
    linia = org_lista[l]
    if l != len(org_lista)-1 and org_lista[l+1].startswith('Tytuł:'): #generowanie własnego numeru, podmienianie w linii
        linia = str(licznik) + '.\n'
        licznik += 1
    if '[uwaga:' in linia:
        linia = linia.partition('[')[0] + '\n'
    lista.append(linia)
    nowalista.write(linia)

autorzy = []
wydawcy = []

#tworzenie txt
for i in range(len(lista)):
    #sys.stdout.write(f'\r' + (i*10//len(lista))*'▓' + (8-i*10//len(lista)+1)*'░' + f' {i*100//len(lista)+1}%')
    sys.stdout.write(f'\rtworzenie plików: {int((i+1)/len(lista)*100)}%')
    sys.stdout.flush()
    linia = lista[i]
    linia = linia.strip()
    if linia.endswith('.') and len(linia) < 6: #wykrywanie początku sprawy
        sprawa = open(f"{lista[i].strip().replace('.','')}.txt", "w", encoding='utf8') #tworzenie pliku

        #init
        sprawa.write(f';"pl"\n')

        #uwagi - dziedziczone
        sprawa.write(f'"uwagi";"Publikacja dofinansowana ze środków budżetu państwa w ramach programu Ministra Edukacji i Nauki pod nazwą „Nauka dla Społeczeństwa” nr projektu NdS/529607/2021/2021 kwota dofinansowania 1.347.970 zł całkowita wartość projektu 1.347.970 zł”."\n')

        #tytuł
        sprawa.write(f'"Title";"{lista[i+1][7::].strip()}"\n')

        #słowa kluczowe
        klucze = []
        słowa_kluczowe = lista[i + 2][24::].split(',')
        for słowo in słowa_kluczowe:

            if słowo.startswith('(') and słowo.endswith(')'):
                słowo = słowo.replace('(','')
                słowo = słowo.replace(')','')
            if słowo.startswith(' '):
                słowo = słowo[1::]
            klucze.append(słowo.strip())
            sprawa.write(f'"Subject";"{słowo.strip()}"\n')

        #dodatkowe słowa kluczowe i publisher

        #DO AUTORÓW W JEDNEJ LINIJCE

        # for j in range(8,0,-1): #łapanie nowego actum i autorów
        #     if 'Actum' in lista[i - j] or '[Actum' in lista[i - j]:
        #         autorzy = []
        #         wydawcy = []
        #         if '.\n' in lista[i - j + 2]:
        #             # print(1, lista[i-j+0])
        #             # print(2, lista[i - j + 1])
        #             # print(3, lista[i - j + 2])
        #             autorzy = lista[i-j+1].split(";")
        #             wydawcy = lista[i - j + 1].split(";")
        #         wydawcy.append(lista[i-j].strip())
        #
        #         # for k in range(j-1, 1, -1): #dodawanie autorów do listy
        #         #     wydawcy.append(lista[i - k].strip())
        #         #     autorzy.append(lista[i - k].strip())
        #         break
        #
        # for klucz in autorzy:
        #     sprawa.write(f'"Subject";"{klucz.strip()}"\n')
        #
        # for wydawca in wydawcy:
        #     sprawa.write(f'"Publisher";"{wydawca.strip()}"\n')

        #DLA AUTORÓW W INNYCH LINIJKACH


        for j in range(10,0,-1): #łapanie nowego actum i autorów
            if 'Actum' in lista[i - j] or '[Actum' in lista[i - j]:
                autorzy = []
                wydawcy = []
                for k in range(j,0,-1): #dodawanie wydawców do listy
                    if lista[i - k].strip() != '':
                        wydawcy.append(lista[i - k].strip())
                for k in range(j-1, 0, -1): #dodawanie autorów do listy
                    if lista[i - k].strip() != '':
                        #autor = lista[i - k].split('–')[0]
                        autorzy.append(lista[i - k].strip())
                break

        for klucz in autorzy:
            sprawa.write(f'"Subject";"{klucz.strip()}"\n')

        for wydawca in wydawcy:
            sprawa.write(f'"Publisher";"{wydawca.strip()}"\n')

        # if 'Paginacja:' not in lista[i-1] and 'Actum' not in lista[i-1]:
        #     wydawcy = lista[i - 1].split(';')
        #     Actum = lista[i - 2]
        #
        # elif 'Actum' in lista[i-1]:
        #     wydawcy = []
        #     Actum = lista[i - 1]
        #
        # for wydawca in wydawcy:
        #     sprawa.write(f'"Subject";"{wydawca.strip()}"\n')
        #
        # sprawa.write(f'"Publisher";"{Actum.strip()}"\n')
        # for wydawca in wydawcy:
        #     sprawa.write(f'"Publisher";"{wydawca.strip()}"\n')

        #data
        sprawa.write(f'"Date";"{lista[i + 3][34::].strip()}"\n')

        #zespół - dziedziczone
        sprawa.write(f'"nazwazes";"Sąd Grodzki Przemyski (1462-1784) [zespół 13, opis 1]"\n')
        #sprawa.write(f'"nazwazes";"Sąd Grodzki Przemyski (1462-1784) [zespół {lista[i + 7][15::].strip()}]"\n')

        #archiwum - dziedziczone
        #sprawa.write(f'"Archiwum";"{lista[i + 6][10::].strip()}"\n')
        sprawa.write(f'"Archiwum";"Centralne Państwowe Archiwum Historyczne Ukrainy we Lwowie / Центральний державний історичний архів України, Львів"\n')

        #prawa - dziedziczone
        sprawa.write(f'"Rights";"Domena publiczna"\n')

        #typ - dziedziczone
        sprawa.write(f'"Type";"{lista[i + 4][12::].strip()}"\n')
        #sprawa.write(f'"Type";"rękopis"\n')

        #format - dziedziczone
        sprawa.write(f'"Format";"pdf"\n')

        #sygnatura
        sprawa.write(f'"sygnatura";"{lista[i + 8][11::].strip()}"\n')
        #sprawa.write(f'"sygnatura";"34"\n')

        #język
        języki = lista[i + 5][7::].split(',')
        for język in języki:
            if język.startswith(' '):
                język = język[1::]
            sprawa.write(f'"Language";"{język.strip()}"\n')

        #paginacja
        sprawa.write(f'"paginacja";"{lista[i + 9][11::].strip()}"\n')

        #tytuł grupowy
        sprawa.write(f'"GroupTitle";"CPAH, Lwów, Sygn. {lista[i + 8][11::].strip()}"\n')


        '''
        0 - id
        1 - Tytuł: (7)
        2 - Temat i słowa kluczowe: (24)
        3 - Data wydania/powstania dokumentu: (34)
        4 - Typ zasobu: (12)
        5 - Język: (7)
        6 - Archiwum: (10)
        7 - Numer zespołu: (15)
        8 - Sygnatura: (11)
        9 - Paginacja: (11)
        '''