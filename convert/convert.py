import requests
import json
import os
import smtplib
import mimetypes
from email.message import EmailMessage


def choose():
    print('\n'
          '> (1) Word\n'
          '> (2) PowerPoint\n'
          '> (3) Excel\n'
          '> (4) Bild\n')

    while True:
        user_input = input('Auswahl > ')
        if user_input.isdigit() and 1 <= int(user_input) <= 5:
            return int(user_input)


def conv():
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
            ftype: open(input("Pfad > "), 'rb')
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

    sender_email = "afb.goodnotes@gmail.com"
    receiver_email = "af.brinkmann@icloud.com"
    password = gmpw

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)

    subject = "GOODNOTES"
    body = "GOODNOTES"

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)

    with open('result.pdf', 'rb') as fp:
        file_data = fp.read()
        maintype, _, subtype = (mimetypes.guess_type('result.pdf')[0] or 'application/octet-stream').partition("/")
        message.add_attachment(file_data, maintype=maintype, subtype=subtype, filename='result.pdf')

    server.send_message(message)
    server.quit()

    print("SENT")
    os.remove('result.pdf')


choice = 0
ftype = ''
while choice == 0:
    choice = choose()

if choice == 1 or choice == 2 or choice == 3:
    ftype = 'document'
    conv()
elif choice == 4:
    ftype = 'image'
    conv()
