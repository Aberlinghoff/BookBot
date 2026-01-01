def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def num_of_words(text):
    print(f"Found {len(text.split())} words")

def main():
    print(get_book_text("books/frankenstein.txt"))
    num_of_words(get_book_text("books/frankenstein.txt"))

main()


