import tkinter as tk
import requests

root = tk.Tk()
root.title("URL-Shortener")
root.geometry("800x600")
root.resizable(width=False, height=False)


def short_url():
    long_url = long_url_input.get()
    custom = custom_input.get()

    api_url = f"https://api.lnk.pw/1.0/public/lnk.pw/link?long={long_url}&custom={custom}"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if data.get('status') == 'ok':
            short_url = data['link']
            info_label.config(text=f'Verkürzte URL > {short_url}')
        else:
            error_id = data.get('error_id')
            error_str = data.get('error_str')
            info_label.config(text=f'Fehler bei der API-Antwort: {error_id} - {error_str}')
    else:
        info_label.config(text=f'Fehler bei der API-Anfrage:  {response.status_code}')


intro_short = tk.Label(root, font=('SF Pro Display', 40), text='URL-Shortener')
intro_short.pack(pady=30)

long_url_input = tk.Entry(root, font=('SF Pro Display', 20))
long_url_input.pack(pady=40)

custom_input = tk.Entry(root, font=('SF Pro Display', 20))
custom_input.pack()

send = tk.Button(root, text="Kürzen", font=('SF Pro Display', 15), command=short_url)
send.pack(pady=10)

info_label = tk.Label(root, text='---', font=('SF Pro Display', 15))
info_label.pack(pady=20)

root.mainloop()
