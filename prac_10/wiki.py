"""
Practical 10
Wikipedia API and Python Library
"""
import wikipedia


def main():
    """Search and display Wikipedia page information based on user input."""
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary[:1000])
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10])

        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        title = input("Enter page title: ").strip()

    print("Thank you.")


if __name__ == "__main__":
    main()
