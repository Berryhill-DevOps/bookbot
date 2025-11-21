import sys
from stats import get_word_count, get_char_count, sort_char_count

def get_book_text(book):
    with open(book, 'r', encoding="utf-8") as f:
        file_contents = f.read()
    f.closed
    return file_contents

def main():
    book_filepath = sys.argv[1]
    num_words = get_word_count(get_book_text(book_filepath))
    num_chars = get_char_count(get_book_text(book_filepath))
    sorted_chars = sort_char_count(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()