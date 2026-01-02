from stats import num_of_words, num_of_characters

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def main():
    print(get_book_text("books/frankenstein.txt"))
    num_of_words(get_book_text("books/frankenstein.txt"))
    print(num_of_characters(get_book_text("books/frankenstein.txt")))
main()


