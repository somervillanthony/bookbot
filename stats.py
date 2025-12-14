def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words

def get_num_chars(book_text):
    char_dictionary = {}
    for letter in book_text:
        lowered = letter.lower()
        if lowered in char_dictionary:
             char_dictionary[lowered] += 1
        else:
             char_dictionary[lowered] = 1
    return char_dictionary

def sort_num_chars(char_dictionary):
    sort_char_list = []
    for char in char_dictionary:
        if char == " ":
            continue
        temp_dictionary = {}
        temp_dictionary["char"] = char
        temp_dictionary["num"] = char_dictionary[char]
        sort_char_list.append(temp_dictionary)
    sort_char_list.sort(reverse=True,key=sort_on)
    return sort_char_list
    

def sort_on(items):
    return items["num"]