import sys
from stats import get_num_words, get_num_chars, sort_num_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    char_dictionary = get_num_chars(book_text)
    sorted_char_list = sort_num_chars(char_dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char_list:
        if char["char"].isalpha() == False:
            continue
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


main()