import tkinter as tk

name = input('Vorname > ')
lastname = input('Nachname > ')
password = input('Passwort > ')
pwrepeat = input('Wiederholen > ')

while pwrepeat != password:
    print("Keine Übereinstimmung")
    password = input('Passwort > ')
    pwrepeat = input('Wiederholen > ')

email = input('Email > ')
agb = input('AGB (y/n) > ')

while agb != 'y':
    print("Zustimmung erforderlich")
    agb = input('AGB (y/n) > ')

newsletter = input('Newsletter (y/n) > ')

agb = True
if newsletter == 'y':
    newsletter = True
else:
    newsletter = False


with open('nutzerdaten.csv', 'a') as file:
    file.write(f'{name},{lastname},{password},{email},{agb},{newsletter}\n')
print('\nRegistrierung erfolgreich')