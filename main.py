"""This is a program for analyzing text files"""


def main():
    """Main Function"""
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    character_count.sort(reverse=True, key=lambda x: x["count"])
    print(character_count)
    print_report(word_count)


def get_book_text(path):
    """Function to read text of a file"""
    with open(path, encoding="utf-8") as f:
        return f.read()


def get_word_count(text):
    """Function to count words in file"""
    words = text.split()
    return len(words)


def get_character_count(text):
    """Function to count occurances of each letter in the file"""
    lowercase = text.lower()
    character_count = []
    for char in set(lowercase):
        if char.isalpha():
            count = lowercase.count(char)
            character_count.append({"letter": char, "count": count})
    return character_count


def print_report(word_count):
    """Function to print the file analysis"""
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")


main()
