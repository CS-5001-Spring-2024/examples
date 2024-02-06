VOWELS = ['a', 'e', 'i', 'o', 'u']
def is_vowel(character: str) -> bool:
    return character in VOWELS

def count_vowels(phrase: str) -> int:
    vowels = 0
    for char in phrase:
        if is_vowel(char):
            vowels += 1
    return vowels

def get_phrase() -> str:
    return input('Enter a phrase, and I\'ll count the vowels: ')

def main():
    # phrase = 'the quick brown fox'
    phrase = get_phrase()
    result = count_vowels(phrase)
    print(result)

    phrase = 'jumped over the lazy dog'
    print(count_vowels(phrase))

if __name__ == '__main__':
    main()