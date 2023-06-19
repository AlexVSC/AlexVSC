import tkinter as tk

name = input('Vorname > ')
lastname = input('Nachname > ')
password = input('Passwort > ')
email = input('Email > ')

found = False

with open('nutzerdaten.csv', 'r') as file:
    for line in file:
        line = line.strip()
        data = line.split(',')
        if (
            data[0] == name and
            data[1] == lastname and
            data[2] == password and
            data[3] == email
        ):
            found = True
            agb_accepted = data[4]
            newsletter_subscribed = data[5]
            break

if found:
    print('Login erfolgreich')
    if agb_accepted == 'True':
        print('AGB > Akzeptiert')
    else:
        print('AGB > Nicht akzeptiert')
    if newsletter_subscribed == 'True':
        print('Newsletter > Abonniert')
    else:
        print('Newsletter > Nicht abonniert')
else:
    print('Login fehlgeschlagen')