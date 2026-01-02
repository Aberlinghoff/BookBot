def num_of_words(text):
    words = text.split()
    return len(words)

def num_of_characters(text):
    characters = {}
    new_text = text.lower()
    for char in new_text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def dict_num(items):
    return items["num"]


def report(dictionary):
    list_of_chars = []
    for key, value in dictionary.items():
        list_of_chars.append({"char": key,"num": value })
    list_of_chars.sort(reverse=True, key=dict_num)
    return list_of_chars