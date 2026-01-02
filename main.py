from stats import num_of_words, num_of_characters, report
import sys

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

if len(sys.argv) < 2:
    print("Usage: python main.py <path>")
    sys.exit(1)
book_path = sys.argv[1]

text = get_book_text(book_path)



def main():


    print("============ BOOKBOT ============\n"
    "Analyzing book found at books/frankenstein.txt...\n"
    "----------- Word Count ----------")
    print(f"Found {num_of_words(text)} total words")
    print("--------- Character Count -------")

    chars = num_of_characters(text)
    sorted_chars = report(chars)

    for item in sorted_chars:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")

    print("============= END ===============")
main()


