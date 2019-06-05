#!/usr/bin/env python3

'''
Calculator - simple program with functionalities such as:
adding, substraction, multiplying and division. It also saves results
to a backend .txt file in the same directory.

My first own project ever.
Written: 23.11.2018

Chris Brymer, author
'''


import os
from datetime import datetime


class Calculator():

    '''Calculator class that has methods such as:
    add, substract, multiplication and division'''

    def add(self):
        print('Dodawanie:')
        self.a = float(input('Pierwsza liczba: '))
        self.b = float(input('Druga liczba: '))
        self.result = self.a + self.b
        self.sign = ' + '
        return self.result


    def substract(self):
        print('Odejmowanie:')
        self.a = float(input('Pierwsza liczba: '))
        self.b = float(input('Druga liczba: '))
        self.result = self.a - self.b
        self.sign = ' - '
        return self.result


    def multiply(self):
        print('Mnożenie:')
        self.a = float(input('Pierwsza liczba: '))
        self.b = float(input('Druga liczba: '))
        self.result = self.a * self.b
        self.sign = ' * '
        return self.result


    def divide(self):
        print('Dzielenie:')
        self.a = float(input('Pierwsza liczba: '))
        self.b = float(input('Druga liczba: '))
        self.result = self.a / self.b
        self.sign = ' / '
        return self.result


    def save(self):
        path = (os.path.join(os.getcwd(),'historia_kalkulatora.txt'))
        with open(path,'a') as file:
            if os.path.getsize(path) == 0:
                file.write('Historia kalkulatora:\n\n')
            file.write(datetime.now().strftime('%Y-%m-%d: %H:%M:%S') +':   '+ str(self.a)+self.sign+str(self.b) + \
                       ' = '+str(self.result)+'\n')


def wybór_opcji():

    menu_text = '''
        Wybierz rodzaj działania:
        1 - dodawanie;
        2 - odejmowanie;
        3 - mnożenie;
        4 - dzielenie;
        exit - wyjście;
        Wybór: '''
    result = input(menu_text)
    while result not in ['1','2','3','4','exit']:
        print('Wybierz jedną z dostępnych opcji!')
        result = input(menu_text)

    return result


hello_sign ='''
 __________________________________
|@                                @|
|   Witam w programie kalkulator!  |
|__________________________________|'''

print(hello_sign)
calc = Calculator()
choice = wybór_opcji()

while choice != 'exit':

    if choice is '1':

        print('\nresult: ',calc.add())
        calc.save()
        choice = wybór_opcji()

    elif choice is '2':
        print('\nresult: ', calc.substract())
        calc.save()
        choice = wybór_opcji()

    elif choice is '3':
        print('\nresult: ', calc.multiply())
        calc.save()
        choice = wybór_opcji()

    elif choice is '4':
        print('\nresult: ', calc.divide())
        calc.save()
        choice = wybór_opcji()

else:
    print('Koniec programu !\n'\
          '----------------------------------------------------')
