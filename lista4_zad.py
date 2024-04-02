import os 


def zad1(directory):
    # current_folder = os.getcwd()
    os.chdir(directory)
    current_content = os.listdir('.')
    print(f"Zawartość wskazanego katalogu: {current_content}")


#zad1('C:/Users/Student s1016/MRog/pythonProject2')


# while True:
#     question = input("Czy mam zmienić katalog? ")
#     if question == "yes":
#         zad1('C:/Users/Student s1016/MRog/pythonProject2')
#         exit()
#     else:
#         exit()



def zad3():
    #a)
    ur_directory = os.getcwd()
    os.makedirs(ur_directory + '/folder')
    print(ur_directory)
    os.chdir(ur_directory + '/folder')
    plik1 = open('Lab1.doc', 'w')
    plik2 = open('Lab2.doc', 'w')
    plik3 = open('Lab3.doc', 'w')
    content_of_folder = os.listdir()
    print(content_of_folder)
    #b)
    doc_files = [file for file in os.listdir() if file.endswith('.doc')]
    print("Pliki z rozszerzeniem *.doc w folderze roboczym:")
    for doc_file in doc_files:
        print(doc_file)


#zad3()


### ZAD 4 v------------------------------v

# os.makedirs('StudentDoc', exist_ok=True)
# os.makedirs('StudentObrazy', exist_ok=True)

# with open(os.path.join('StudentDoc', 'tekst1.txt'), 'w') as file:
#     file.write('To jest tekstowy plik 1.nijhgfeadfiahnbinvhjfrdavfadinjhivanfjd')
# with open(os.path.join('StudentDoc', 'tekst2.txt'), 'w') as file:
#     file.write('To jest tekstowy plik 2.bhuvfehbuvdshbsid')

# with open(os.path.join('StudentObrazy', 'obraz1.jpg'), 'wb') as file:
#     file.write(b'Placeholder dla obrazu 1.')
# with open(os.path.join('StudentObrazy', 'obraz2.jpg'), 'wb') as file:
#     file.write(b'Placeholder dla obrazu 2.')

# def wyswietl_zawartosc(folder):
#     print(f'Zawartość folderu {folder}:')
#     for item in os.listdir(folder):
#         item_path = os.path.join(folder, item)
#         if os.path.isfile(item_path):
#             rozmiar = os.path.getsize(item_path)
#             print(f'- {item} (rozmiar: {rozmiar} bajtów)')

# #print(ur_directory + '/StudentDoc')
# ur_directory = os.getcwd()

# wyswietl_zawartosc(ur_directory + '/StudentDoc')
# wyswietl_zawartosc(ur_directory + '/StudentObrazy')


def zad5():
    ur_directory = os.getcwd()
    os.makedirs('katalog')
    sciezka = os.getcwd() + '/katalog'
    os.rename(sciezka, ur_directory + '/kot')


#zad5()

def zad6():
    filename = '3listy.data'
    fruits = ['jabłka', 'maliny', 'winogrona']
    veggies = ['pomidor', 'ogórek', 'sałata']
    sweets = ['cukierki', 'ciasto', 'czekolada']
    f1 = open(filename, 'wb')
    pickle.dump(fruits, f1)
    pickle.dump(veggies, f1)
    pickle.dump(sweets, f1)
    f1.close()
    f2 = open(filename, 'rb')
    list1 = pickle.load(f2)
    list2 = pickle.load(f2)
    list3 = pickle.load(f2)
    lists = list1 + list2 + list3
    for rzecz in lists:
        print(rzecz)


#zad6()



## Wariant z zapisem do pliku + pack()
def zad7():
    f1 = open('zad_7_plik2.dat','wb') # litera b oznacza zapis danych binarnych
    long_number = pack('l',123456789)
    f1.write(long_number)
    f1.close()

## Odczyt danych z pliku
    f2 = open("zad_7_plik2.dat", "rb")   # litera b oznacza odczyt danych binarnych
    print(unpack('l',f2.read()))
    f2.close()


#zad7()

import re

def zad9():

    ur_directory = os.getcwd()
    os.makedirs('pliki tekstowe', exist_ok=True)
    os.chdir(ur_directory + '/pliki tekstowe')
    f1 = open('Tekst1ID_ABC.txt', 'w')
    f1.write('Dynamiczny rozwój światowego rynku mediów elektronicznych, pojawienie się na nim nowych, przenikających się środków przekazu i łączności, tworzy obecnie bardzo złożoną rzeczywistość. Obowiązujący u nas system regulacyjny w sferze masowego komunikowania jest ciągle zorientowany na utożsamianie mediów elektronicznych z radiem i telewizją, chociaż dotychczasowy podział między radiofonią i telewizją a łącznością wyraźnie się załamał. Cechy tradycyjnego komunikowania masowego zmienia cyfryzacja i wynikający z niej proces konwergencji radia i telewizji oraz telekomunikacji i informatyki. Z jednej strony technologie telekomunikacyjne można wykorzystywać do upowszechniania zawartości mediów masowych (rozprowadzanie programów RTV w internecie, łączenie w multipleksach programów RTV z usługami dodatkowymi, wykorzystywanie satelitów telekomunikacyjnych do celów radiodyfuzyjnych czy infrastruktury telefonicznej do przekazu programu lub muzyki). Z drugiej strony, media stają się nośnikiem łączności porozumiewawczej (na przykład przy wykorzystywaniu TV kablowej dla celów telefonii). ?Proces cyfryzacji i konwergencji oraz kształtowanie się nowych technik informacyjno-komunikacyjnych wymaga więc objęcia polityką państwa zdecydowanie szerszego aspektu spraw, niż tylko funkcjonowanie nadawców radiowych i telewizyjnych.')
    f1.close()
    f2 = open('Tekst2ID_0405.txt', 'w')
    f2.write('Potrzebujemy nowej, spójnej i całościowej regulacji, uwzględniającej nie tylko wszystkie elementy nakładające się na funkcjonowanie rynku w Polsce, ale także dostrzegającej ten rynek w perspektywie wspólnego rynku europejskiego i panującej na nim konkurencji.Dwie podstawowe przesłanki, jakie trzeba wziąć pod uwagę, to orientacja na przyszłość oraz troska o kompleksowe podejście do mediów w kontekście szerokiego procesu przemiany cywilizacyjnej, gospodarczej i technicznej.')
    f2.close()
    f3 = open('Tekst3ID_607.txt', 'w')
    f3.write('Problemem wymagającym odrębnego podkreślenia jest aktywne uczestniczenie państwa w tworzeniu i realizacji polityki audiowizualnej oraz polityki na rzecz rozwoju społeczeństwa informacyjnego w ramach Unii Europejskiej i innych organizacji międzynarodowych. Ze względu na swój charakter i cele, polityka w dziedzinie mediów elektronicznych powinna być skoordynowana z innymi planami i strategiami państwa. W przeciwnym razie naszemu państwu grozi poważny regres w dziedzinie, od której w istotny sposób zależy nasz rozwój kulturowy i gospodarczy. „Mimo szumnych zapowiedzi, rządzące obecnie Polską ugrupowanie (wraz z koalicjantami) nie podjęło żadnych kroków zmierzających we wskazanym powyżej kierunku. Jeszcze raz się okazało, że kwestie personalne wyczerpują praktycznie zainteresowanie tym problemem. Trudno więc spodziewać się w jakiejś konkretnej perspektywie projektów ustaw (nie wspominając o narodowych planach rozwojowych), które by zmieniły obecny stan rzeczy. Na szczęście pozostaje jeszcze inicjatywa obywatelska.')
    f3.close()
    f4 = open('Tekst4ID_ABC.txt', 'w')
    f4.write('Lech Jaworski Analiza Rynek mediów elektronicznych domaga się zmian Dogonić EuropęNasze prawo medialne nie przystaje do rzeczywistości i hamuje rozwój. Dlatego wymaga gruntownej przebudowy. Politycy ze wszystkich ugrupowań szermują słowem „rynek”. Łatwo się używa haseł dobrze brzmiących (zwłaszcza w uszach wyborców), trudniej się je realizuje. Oczywiście zakładając, że posługujący się nimi rozumieją, o czym mówią. Ostatnie założenie wydaje się zbyt optymistyczne, jeżeli chodzi o rynek mediów elektronicznych. Nie tylko nie dostrzega się związków funkcjonujących na tym rynku podmiotów z gospodarką, ale w większości wypadków „rynek” utożsamia się z bazarem, na którym odbywają się polityczne targi o obsadę stanowisk w mediach publicznych.')
    f4.close()
    f5 = open('Tekst5ID_DEF.txt', 'w')
    f5.write('Cieszy się ona dużym zainteresowaniem nie tylko poszczególnych rządów krajowych, ale też struktur działających w ramach Unii Europejskiej. Polityka wspólnotowa traktuje media głównie jak jeden z działów gospodarki i określa jako „usługi w ogólnym interesie gospodarczym”. Jednym z podstawowych założeń przyjętej w marcu 2000 r. strategii lizbońskiej, będącej obecnie najważniejszym programem społeczno-gospodarczym UE, jest postrzeganie komunikacji elektronicznej (tj. zbiorczo telekomunikacji i mediów elektronicznych) jako narzędzia tworzącego społeczeństwo informacyjne oraz gospodarkę opartą na wiedzy. Warunkiem skutecznego stosowania tego narzędzia ma być liberalizacja rynku. Zasadniczym elementem strategii lizbońskiej stało się opracowanie i wdrożenie zupełnie nowego pakietu regulacyjnego obejmującego jednolitymi przepisami cały sektor komunikacji elektronicznej: mediów, telekomunikacji i teleinformatyki. Zapomniany sektor ?U nas temat traktuje się zupełnie marginalnie, czego jaskrawym dowodem jest choćby pomijanie go w naszych narodowych planach i strategiach rozwoju. Musi to z czasem doprowadzić (właściwie już doprowadziło) do osłabienia naszych możliwości w tym zakresie i, co najzupełniej logiczne, do pozbawienia rodzimego rynku skutecznych środków obrony przed konkurencją zagraniczną.')
    f5.close()
    # a)
    pliki = os.listdir()
    print("Podpunkt a): ")
    print(pliki)
    # b)
    liczba_wyrazow = 0
    for plik in pliki:
        if plik.endswith('ABC.txt'):
            with open(plik, 'r') as file:
                tekst = file.read()
                wyrazy = re.findall(r'\b\w{3,}\b', tekst)
                liczba_wyrazow += len(wyrazy)
    print("Podpunkt b): Ilość wyrazów w plikach zakończonych na ABC: ")
    print(liczba_wyrazow)
    # a) dodatkowe
    liczba_plikow = 0
    for plik in pliki:
        if 'ID_0' in plik:
            liczba_plikow += 1
    print(f"Liczba takich plików gdzie w identyfikatorze jest ID_0 to: {liczba_plikow}")
    # b) dodatkowe

    liczba_slow = 0
    for plik in pliki:
        if '0' not in plik:
            with open(plik, 'r') as file:
                tekst = file.read()
                #print(tekst)
                wyrazy = re.findall(r'\b\w+\b', tekst)
                liczba_slow += len(wyrazy)
                print(f"Liczba słów w pliku to: {liczba_slow}")


zad9()