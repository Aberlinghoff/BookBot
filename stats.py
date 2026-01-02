def num_of_words(text):
    print(f"Found {len(text.split())} words")


def num_of_characters(text):
    characters = {}
    new_text = text.lower()
    for char in new_text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters
