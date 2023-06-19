import requests
import json
import os
import smtplib
import mimetypes
from email.message import EmailMessage
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import sv_ttk

root = tk.Tk()
root.title('GoodNotes')
root.geometry('400x400')
root.resizable(width=False, height=False)

heading = tk.Label(root, text='GoodNotes', font=('Arial', 30))
heading.pack(pady=10)

subheading = tk.Label(root, text='Dateiupload', font=('Arial', 18))
subheading.pack(pady=10)

radio_var = tk.IntVar()
ftype = ''
file_path = ''
file_selected = False
file_type_chosen = False

frame = ttk.Frame(root)
frame.pack()


def choose():
    global ftype, file_type_chosen
    selected_option = radio_var.get()
    if selected_option == 1 or selected_option == 2 or selected_option == 3:
        ftype = 'document'
        print(ftype)
    elif selected_option == 4:
        ftype = 'image'
        print(ftype)
    file_type_chosen = True


def select_file():
    global file_path, file_selected
    file_path = filedialog.askopenfilename()
    if file_path:
        print(file_path)
        file_selected = True


def startconvert():
    if file_selected and file_type_chosen:
        conv()
    else:
        feedback_lbl.config(text='Dateityp und Dateipfad zuerst wählen')


def conv():
    feedback_lbl.config(text='Konvertierung gestartet')
    global file_path, ftype
    instructions = {
        'parts': [
            {
                'file': ftype
            }
        ]
    }

    response = requests.request(
        'POST',
        'https://api.pspdfkit.com/build',
        headers={
            'Authorization': 'Bearer pdf_live_m6kJoP1NcuwMPpgZA7dE0hCk0fgLbwCECbF3xp9iW2k'
        },
        files={
            ftype: open(file_path, 'rb')
        },
        data={
            'instructions': json.dumps(instructions)
        },
        stream=True
    )

    if response.ok:
        with open('result.pdf', 'wb') as fd:
            for chunk in response.iter_content(chunk_size=8096):
                fd.write(chunk)
        send()
    else:
        print(response.text)
        exit()


def send():
    feedback_lbl.config(text='Versenden gestartet')
    gmpw = 'pvpwqzakpxegursa'

    sender_email = 'afb.goodnotes@gmail.com'
    receiver_email = 'me.tygvdq3@goodnotes.email'
    password = gmpw

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)

    subject = 'GOODNOTES'
    body = 'GOODNOTES'

    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.set_content(body)

    with open('result.pdf', 'rb') as fp:
        file_data = fp.read()
        maintype, _, subtype = (mimetypes.guess_type('result.pdf')[0] or 'application/octet-stream').partition('/')
        message.add_attachment(file_data, maintype=maintype, subtype=subtype, filename='result.pdf')

    server.send_message(message)
    server.quit()

    feedback_lbl.config(text='Datei gesendet')
    os.remove('result.pdf')


feedback_frame = ttk.LabelFrame(frame, text='Dateityp')
feedback_frame.grid(row=0, column=0, padx=20, pady=10, sticky='n', rowspan=2)

radio_btn1 = ttk.Radiobutton(feedback_frame, text='Word', variable=radio_var, value=1)
radio_btn1.grid(row=0, column=0, sticky='w', pady=5, padx=5)

radio_btn2 = ttk.Radiobutton(feedback_frame, text='PowerPoint', variable=radio_var, value=2)
radio_btn2.grid(row=1, column=0, sticky='w', pady=5, padx=5)

radio_btn3 = ttk.Radiobutton(feedback_frame, text='Excel', variable=radio_var, value=3)
radio_btn3.grid(row=2, column=0, sticky='w', pady=5, padx=5)

radio_btn4 = ttk.Radiobutton(feedback_frame, text='Bild', variable=radio_var, value=4)
radio_btn4.grid(row=3, column=0, sticky='w', pady=5, padx=5)

sub_btn1 = ttk.Button(feedback_frame, text='Bestätigen', command=choose)
sub_btn1.grid(row=4, column=0, pady=10, padx=20)

filechoose_frame = ttk.LabelFrame(frame, text='Dateiauswahl')
filechoose_frame.grid(row=0, column=1, padx=0, pady=10, sticky='n')

select_btn = ttk.Button(filechoose_frame, text="Datei auswählen", command=select_file)
select_btn.grid(row=0, column=0, pady=21.5, padx=5)

sub_frame = ttk.LabelFrame(frame, text='Bestätigung')
sub_frame.grid(row=1, column=1, padx=0, pady=10, sticky='n')

sub_btn2 = ttk.Button(sub_frame, text='Bestätigen', command=startconvert, style='Accent.TButton')
sub_btn2.grid(row=0, column=0, pady=30, padx=20)

feedback_lbl = ttk.Label(text='Dateityp und Dateipfad wählen')
feedback_lbl.pack(pady=15)

sv_ttk.set_theme("light")

root.mainloop()
