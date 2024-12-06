def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    counted_words = word_count(text)
    counted_characters = character_counter(text)
    book_report(path_to_book)

def word_count(book_to_count):
    return len(book_to_count.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def character_counter(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char not in char_count:
            if char.isalpha() == True:
                char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(dict):
    return dict["num"]

def letter_frequency_sorted_list(char_dict):
    list_of_chars_and_counts =  [{"char": char, "num": count} for char, count in char_dict.items()]
    list_of_chars_and_counts.sort(reverse=True, key=sort_on)
    return list_of_chars_and_counts


def book_report(book_path):
    book_text = get_book_text(book_path)
    book_word_count = word_count(book_text)
    book_character_count = character_counter(book_text)
    book_letter_sorted_list = letter_frequency_sorted_list(book_character_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{book_word_count} words found in the document")
    print("\n")
    for letter in book_letter_sorted_list:
        print(f"The '{letter['char']}' character was found {letter['num']} times")
main()