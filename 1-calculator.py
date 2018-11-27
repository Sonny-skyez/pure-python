'''
My first own project ever.
Written: 23.11.2018 - 23.11.2018
Greetings!
Chris Brymer, author
'''

# Projekt: kalkulator.
# dodawanie, odejmowanie, mnożenie, dzielenie.

import os
from datetime import datetime

class Calculator():


    def dodaj(self):
        print('Dodawanie:')
        self.a = float(input('Pierwsza liczba: '))
        self.b = float(input('Druga liczba: '))
        self.wynik = self.a + self.b
        self.znak = ' + '
        return self.wynik


    def odejmij(self):
        print('Odejmowanie:')
        self.a = float(input('Pierwsza liczba: '))
        self.b = float(input('Druga liczba: '))
        self.wynik = self.a - self.b
        self.znak = ' - '
        return self.wynik


    def pomnoz(self):
        print('Mnożenie:')
        self.a = float(input('Pierwsza liczba: '))
        self.b = float(input('Druga liczba: '))
        self.wynik = self.a * self.b
        self.znak = ' * '
        return self.wynik


    def podziel(self):
        print('Dzielenie:')
        self.a = float(input('Pierwsza liczba: '))
        self.b = float(input('Druga liczba: '))
        self.wynik = self.a / self.b
        self.znak = ' / '
        return self.wynik


    def zapis(self):
        path = (os.path.join(os.getcwd(),'historia_kalkulatora.txt'))
        with open(path,'a') as file:
            if os.path.getsize(path) == 0:

                file.write('Historia kalkulatora:\n\n')

            file.write(datetime.now().strftime('%Y-%m-%d: %H:%M:%S') +':   '+ str(self.a)+self.znak+str(self.b) + \
                       ' = '+str(self.wynik)+'\n')




def wybór_opcji():

    menu_text = '''
        Wybierz rodzaj działania:
        1 - dodawanie;
        2 - odejmowanie;
        3 - mnożenie;
        4 - dzielenie;
        exit - wyjście;
        Wybór: '''

    wynik = input(menu_text)

    while wynik not in ['1','2','3','4','exit']:

        print('Wybierz jedną z dostępnych opcji!')
        wynik = input(menu_text)


    return wynik



komunikat ='''
 __________________________________
|@                                @|
|   Witam w programie kalkulator!  |
|__________________________________|'''

print(komunikat)


calc = Calculator()


choice = wybór_opcji()

while choice != 'exit':

    if choice is '1':

        print('\nWynik: ',calc.dodaj())
        calc.zapis()
        choice = wybór_opcji()

    elif choice is '2':
        print('\nWynik: ', calc.odejmij())
        calc.zapis()
        choice = wybór_opcji()

    elif choice is '3':
        print('\nWynik: ', calc.pomnoz())
        calc.zapis()
        choice = wybór_opcji()

    elif choice is '4':
        print('\nWynik: ', calc.podziel())
        calc.zapis()
        choice = wybór_opcji()


else:
    print('Koniec programu !\n'\
          '----------------------------------------------------')
