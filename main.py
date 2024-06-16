"""This is a program for analyzing text files"""


def main():
    """Main Function"""
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document!")
    print(get_character_count(text))


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
    character_count = {}
    for char in lowercase:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


main()
