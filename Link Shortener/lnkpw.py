import tkinter as tk
import requests


long_url = input('URL > ')
custom = ''
while len(custom) <= 5:
    custom = input('Custom > ')

api_url = f"https://api.lnk.pw/1.0/public/lnk.pw/link?long={long_url}&custom={custom}"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    if data.get('status') == 'ok':
        short_url = data['link']
        print('Verkürzte URL > ', short_url)
    else:
        error_id = data.get('error_id')
        error_str = data.get('error_str')
        print(f'Fehler bei der API-Antwort: {error_id} - {error_str}')
else:
    print('Fehler bei der API-Anfrage:', response.status_code)