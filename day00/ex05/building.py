import sys


def maj_count(object: any) -> int:
    count = 0
    for letter in object:
        if letter.isupper():
            count += 1
    return count


def min_count(object: any) -> int:
    count = 0
    for letter in object:
        if letter.islower():
            count += 1
    return count


def space_count(object: any) -> int:
    count = 0
    for letter in object:
        if letter.isspace():
            count += 1
    return count


def digit_count(object: any) -> int:
    count = 0
    for letter in object:
        if letter.isdigit():
            count += 1
    return count


def punct_count(object: any) -> int:
    ponctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    count = 0
    for letter in object:
        if letter in ponctuations:
            count += 1
    return count


def main():
    """
    Compter le nombre de majuscule, minuscule, ponctuation, espace d'une string

    Args:
        string : string dans laquelle compter le nombre de char
    returns : details de ce qui a ete lu
    """
    try:
        string = ""
        if len(sys.argv) < 2:
            try:
                string = input("What is the text to count?\n")
                string += "\n"
            except EOFError:
                pass
        elif len(sys.argv) == 2:
            if not sys.argv[1]:
                try:
                    string = input("What is the text to count?\n")
                    string += "\n"
                except EOFError:
                    pass
            else:
                string = sys.argv[1]
        else:
            raise AssertionError("Too many arguments")
        print("The text contains", len(string), "characters:")
        print(maj_count(string), "upper letters")
        print(min_count(string), "lower letters")
        print(punct_count(string), "punctuation marks")
        print(space_count(string), "spaces")
        print(digit_count(string), "digits")
    except AssertionError as e:
        print(e)
        sys.exit(1)

    # print("la doc\n", main.__doc__)


if __name__ == "__main__":
    main()
