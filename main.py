from stats import get_word_count, get_char_count

def get_book_text(book):
    with open(book, 'r', encoding="utf-8") as f:
        file_contents = f.read()
    f.closed
    return file_contents

def main():
    num_words = get_word_count(get_book_text(book_filepath))
    num_chars = get_char_count(get_book_text(book_filepath))
    return print(f"Found {num_words} total words & {num_chars}")

book_filepath = "books/frankenstein.txt"
main()