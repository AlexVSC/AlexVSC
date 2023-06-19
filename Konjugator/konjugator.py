import webbrowser

def open_safari_tabs():
    print("Konjugation")
    words = []
    while True:
        line = input("> ")
        if line == "":
            break
        words.append(line.strip())

    for word in words:
        url = f"https://konjugator.reverso.net/konjugation-franzosisch-verb-{word}.html"
        webbrowser.get("safari").open_new_tab(url)

open_safari_tabs()