import requests
import datetime
from fpdf import FPDF

shortname = datetime.datetime.now().strftime("Moodle-Upload-%d_%m_%Y")

key = '0dad00e7f5babf301bb20dbb14657cf229443'
url = input("Link >> ")
name = shortname
r = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url, name))
pdfoutput = 'https://www.cutt.ly/'+shortname

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('helvetica', 'u', 13)
pdf.cell(0, 0, pdfoutput)
pdf.link(x=0, y=0, w=210, h=20, link=pdfoutput)
pdf.output(datetime.datetime.now().strftime("Aufgaben - %d.%m.%Y.pdf"))