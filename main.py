def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        counted_words = word_count(file_contents)
        print(counted_words)

def word_count(book_to_count):
    book_words = book_to_count.split()
    num_book_words = len(book_words)
    return num_book_words

main()