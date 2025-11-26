import wikipedia

def main():
    title = input("Enter page title: ").strip()
    while title != "":
        page = wikipedia.page(title, auto_suggest = False)
        print(page.title)
        print(page.summary[.500])
        print(page.url)



