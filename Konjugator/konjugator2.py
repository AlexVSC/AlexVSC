import tkinter as tk
import webbrowser

root = tk.Tk()
root.title("Konjugator")
root.geometry("800x600")
root.resizable(width=False, height=False)


def create_entry(event=None):
    entry = tk.Entry(root, font=('SF Pro Display', 20))
    entry.pack()
    entry.focus_set()


def open_safari_tabs(event=None):
    words = []
    for entry in root.winfo_children():
        if isinstance(entry, tk.Entry):
            words.append(entry.get().strip())
    for word in words:
        url = f"https://konjugator.reverso.net/konjugation-franzosisch-verb-{word}.html"
        webbrowser.get("safari").open_new_tab(url)


def close_window(event=None):
    root.destroy()


label1 = tk.Label(root, text="Konjugator", font=('SF Pro Display', 30))
label1.pack(padx=20, pady=20)

label2 = tk.Label(root, text="Verben", font=('SF Pro Display', 23))
label2.pack(padx=20, pady=20)

button1 = tk.Button(root, text="Verb hinzufügen", font=('SF Pro Display', 15), command=create_entry)
button1.pack()

button2 = tk.Button(root, text="Konjugation", font=('SF Pro Display', 15), command=open_safari_tabs)
button2.pack()

button3 = tk.Button(root, text="Schließen", font=('SF Pro Display', 15), command=close_window)
button3.pack()

root.bind("<Down>", create_entry)
root.bind("<Up>", open_safari_tabs)
root.bind("<Left>", close_window)
root.bind("<Right>", close_window())

root.mainloop()
