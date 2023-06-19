import requests
import json
import os
import smtplib
import mimetypes
from email.message import EmailMessage
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('GoodNotes')
root.geometry('400x300')
root.resizable(width=False, height=False)

radio_var = tk.IntVar()
ftype = ''
file_path = ''

frame = tk.Frame(root)
frame.pack()


def choose():
    global ftype
    selected_option = radio_var.get()
    if selected_option == 1 or selected_option == 2 or selected_option == 3:
        ftype = 'document'
        print(ftype)
    elif selected_option == 4:
        ftype = 'image'
        print(ftype)


def select_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        print(file_path)


def startconvert():
    conv()


def conv():
    global file_path
    global ftype
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
    gmpw = 'pvpwqzakpxegursa'

    sender_email = 'afb.goodnotes@gmail.com'
    receiver_email = 'af.brinkmann@icloud.com'
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

    print('SENT')
    os.remove('result.pdf')




filetype_frame = tk.LabelFrame(frame, text='Dateityp')
filetype_frame.grid(row=0, column=0, padx=20, pady=10, sticky='n', rowspan=2)

radio_btn1 = tk.Radiobutton(filetype_frame, text='Word', variable=radio_var, value=1)
radio_btn1.grid(row=0, column=0, sticky='w', pady=5, padx=5)

radio_btn2 = tk.Radiobutton(filetype_frame, text='PowerPoint', variable=radio_var, value=2)
radio_btn2.grid(row=1, column=0, sticky='w', pady=5, padx=5)

radio_btn3 = tk.Radiobutton(filetype_frame, text='Excel', variable=radio_var, value=3)
radio_btn3.grid(row=2, column=0, sticky='w', pady=5, padx=5)

radio_btn4 = tk.Radiobutton(filetype_frame, text='Bild', variable=radio_var, value=4)
radio_btn4.grid(row=3, column=0, sticky='w', pady=5, padx=5)

sub_btn1 = tk.Button(filetype_frame, text='Bestätigen', command=choose)
sub_btn1.grid(row=4, column=0, pady=10, padx=20)

filechoose_frame = tk.LabelFrame(frame, text='Dateiauswahl')
filechoose_frame.grid(row=0, column=1, padx=0, pady=10, sticky='n')

select_btn = tk.Button(filechoose_frame, text="Datei auswählen", command=select_file)
select_btn.grid(row=0, column=0, pady=5, padx=5)

sub_btn2 = tk.Button(filechoose_frame, text='Bestätigen')
sub_btn2.grid(row=1, column=0, pady=10, padx=20)

sub_frame = tk.LabelFrame(frame, text='Bestätigung')
sub_frame.grid(row=1, column=1, padx=0, pady=10, sticky='n')

sub_btn3 = tk.Button(sub_frame, text='Bestätigen', command=startconvert)
sub_btn3.grid(row=0, column=0, pady=15, padx=20)

root.mainloop()


