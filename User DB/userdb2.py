import tkinter as tk

root = tk.Tk()
root.title('Registrierung')
root.geometry('800x600')
root.resizable(width=False, height=False)

agb = tk.BooleanVar()
newsletter = tk.BooleanVar()
state_agb = ''
state_newsletter = ''

head = tk.Label(root, text='Registrierung', font=('SF Pro Display', 40))
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
label4 = tk.Label(root, text='Passwort wiederholen', font=('SF Pro Display', 23))
label4.pack()
pwrepeat = tk.Entry(root, font=('SF Pro Display', 20))
pwrepeat.pack()
label5 = tk.Label(root, text='Email', font=('SF Pro Display', 23))
label5.pack()
email = tk.Entry(root, font=('SF Pro Display', 20))
email.pack()

agb_box = tk.Checkbutton(root, text='AGB', variable=agb, onvalue=1, offvalue=0)
agb_box.pack()
newsletter_box = tk.Checkbutton(root, text='Newsletter', variable=newsletter, onvalue=1, offvalue=0)
newsletter_box.pack(pady=15)

status = tk.Label(root, text='---', font=('SF Pro Display', 20))
status.pack()


def registrieren():
    state_agb = str(agb.get())
    state_newsletter = str(newsletter.get())
    if password.get() == pwrepeat.get() and state_agb == 'True':
        with open('nutzerdaten.csv', 'a') as file:
            file.write(f'{name.get()},{lastname.get()},{password.get()},{email.get()},{state_agb},{state_newsletter}\n')
        status.config(text='Registrierung erfolgreich')
    else:
        status.config(text='Registrierung fehlgeschlagen')


submit = tk.Button(root, text='Registrieren', font=('SF Pro Display', 15), command=registrieren)
submit.pack()

root.mainloop()
