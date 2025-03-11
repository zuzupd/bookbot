from stats import print_sorted_character_count, print_header, print_word_count
import sys

def main():    
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        print_header(book_path)
        print_word_count(book_path)
        print_sorted_character_count(book_path)
main()