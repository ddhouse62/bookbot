def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    counted_words = word_count(text)
    print(counted_words)

def word_count(book_to_count):
    return len(book_to_count.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()