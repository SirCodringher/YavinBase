
#1 opcja
wyraz = input('Wpisz frazę: ')

def palindrom(wyraz):
    return wyraz == wyraz[::-1]
print('Wyraz jest palindromem:', palindrom(wyraz))

