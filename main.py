import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words, count_letters, sort_characters

def main():
    filepath = book_path
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    letter_count = count_letters(book_text)
    sorted_chars = sort_characters(letter_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]

        if char.isalpha():
            count = char_dict["count"]
            print(f"{char}: {count}")

    print("============= END ===============")

main()