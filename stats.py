def get_book_test(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    text = text.lower()
    counts = {}
    for character in text:
        counts[character] = counts.get(character, 0) + 1
    return counts

def sort_by_count(count):
    cleaned_dict = {}
    for key, count in count.items():
        if key.isalpha():
            cleaned_dict[key] = count
    sorted_dict = dict(sorted(cleaned_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

def print_sorted_character_count(book_path):
    print("--------- Character Count -------")
    for key, count in sort_by_count(count_chars(get_book_test(book_path))).items():
        print(key + ":", count)
    print("============= END ===============")

def print_header(filepath):
    print("============ BOOKBOT ============")
    print("Analyzing book found at", filepath, "...")

def print_word_count(book_path):
    print("----------- Word Count ----------")
    print("Found", count_words(get_book_test(book_path)), "total words")