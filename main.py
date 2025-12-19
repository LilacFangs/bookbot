import sys
def main():
    from stats import book_word_count
    from stats import book_character_count
    from stats import book_character_sort

    # this if/else statement will stop the program if the proper number of inputs aren't entered.
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        word_count = book_word_count(book_text)
        character_counts = book_character_count(book_text)
        sorted_character_counts = book_character_sort(character_counts)

    # the following prints the report of word count and character distribution per the assignment's instruction's exact format.
        print(f"============ BOOKBOT ============\r\nAnalyzing book found at {book_path}...\r\n----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for character_dictionary in sorted_character_counts:
            individual_character = character_dictionary["char"]
            individual_character_count = character_dictionary["num"]
            print(f"{individual_character}: {individual_character_count}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        return f.read()
main()