def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    counted_words = word_count(text)
    counted_characters = character_counter(text)
    print(counted_characters)

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
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    return char_count

main()