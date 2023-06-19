import smtplib

gmpw = 'pvpwqzakpxegursa'

# E-Mail-Konfiguration
sender_email = "afb.goodnotes@gmail.com"
receiver_email = "af.brinkmann@icloud.com"
password = gmpw

# Verbindung zum SMTP-Server herstellen
smtp_server = "smtp.gmail.com"
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, password)

# E-Mail-Inhalt erstellen
subject = "GOODNOTES"
body = "GOODNOTES"

# E-Mail-Header erstellen
headers = f"From: {sender_email}\r\nTo: {receiver_email}\r\nSubject: {subject}\r\n"

# E-Mail-Nachricht erstellen
message = headers + "\r\n" + body

# E-Mail senden
server.sendmail(sender_email, receiver_email, message)
server.quit()

print("SENT")
