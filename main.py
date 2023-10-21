def main():
    text = read_text()
    words = get_words(text)
    letters = get_letters(text)

    print("------ Begin report on Frakenstein ------")
    print(f"There are {words} in this book")
    print("And here is the distribution of letters")
    for pair in letters:
        print(f"The letter {pair[0]} was found {pair[1]} times")


def read_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def get_words(text):
    words = text.split()
    return len(words)


def get_letters(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter.isalpha():
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
    sortLetterDict = sorted(letters.items(), reverse=True, key=lambda x: x[1])
    return sortLetterDict


main()
