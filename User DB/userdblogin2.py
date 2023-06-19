import tkinter as tk

root = tk.Tk()
root.title('Login')
root.geometry('800x600')
root.resizable(width=False, height=False)

agb = tk.BooleanVar()
newsletter = tk.BooleanVar()
state_agb = ''
state_newsletter = ''

head = tk.Label(root, text='Login', font=('SF Pro Display', 40))
head.pack(pady=25)
label1 = tk.Label(root, text='Name', font=('SF Pro Display', 23))
label1.pack()
name = tk.Entry(root, font=('SF Pro Display', 20))
name.pack()
label2 = tk.Label(root, text='Nachname', font=('SF Pro Display', 23))
label2.pack()
lastname = tk.Entry(root, font=('SF Pro Display', 20))
lastname.pack()
label3 = tk.Label(root, text='Passwort', font=('SF Pro Display', 23))
label3.pack()
password = tk.Entry(root, font=('SF Pro Display', 20))
password.pack()
label5 = tk.Label(root, text='Email', font=('SF Pro Display', 23))
label5.pack()
email = tk.Entry(root, font=('SF Pro Display', 20))
email.pack()
label_agb = tk.Label(root, text='', font=('SF Pro Display', 13))
label_agb.pack()
label_newsletter = tk.Label(root, text='', font=('SF Pro Display', 13))
label_newsletter.pack()

status = tk.Label(root, text='---', font=('SF Pro Display', 20))
status.pack()


def anmeldung():
    found = False
    agb_accepted = ''
    newsletter_subscribed = ''
    with open('nutzerdaten.csv', 'r') as file:
        for line in file:
            line = line.strip()
            data = line.split(',')
            if (
                    data[0] == name.get() and
                    data[1] == lastname.get() and
                    data[2] == password.get() and
                    data[3] == email.get()
            ):
                found = True
                agb_accepted = data[4]
                newsletter_subscribed = data[5]
                break

    if found:
        status.config(text='Login erfolgreich')
        if agb_accepted == 'True':
            label_agb.config(text='AGB > Akzeptiert')
        else:
            label_agb.config(text='AGB > Nicht akzeptiert')
        if newsletter_subscribed == 'True':
            label_newsletter.config(text='Newsletter > Abonniert')
        else:
            label_newsletter.config(text='Newsletter > Nicht abonniert')
    else:
        status.config(text='Login fehlgeschlagen')


submit = tk.Button(root, text='Login', font=('SF Pro Display', 15), command=anmeldung)
submit.pack()

root.mainloop()
