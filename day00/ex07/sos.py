import sys

NESTED_MORSE = {
    'A': '.- ',
    'B': '-... ',
    'C': '-.-. ',
    'D': '-.. ',
    'E': '. ',
    'F': '..-. ',
    'G': '--. ',
    'H': '.... ',
    'I': '.. ',
    'J': '.--- ',
    'K': '-.- ',
    'L': '.-.. ',
    'M': '-- ',
    'N': '-. ',
    'O': '--- ',
    'P': '.--. ',
    'Q': '--.- ',
    'R': '.-. ',
    'S': '... ',
    'T': '- ',
    'U': '..- ',
    'V': '...- ',
    'W': '.-- ', 
    'X': '-..- ',
    'Y': '-.-- ',
    'Z': '--.. ',
    '0': '----- ',
    '1': '.---- ',
    '2': '..--- ',
    '3': '...-- ',
    '4': '....- ',
    '5': '..... ',
    '6': '-.... ',
    '7': '--... ',
    '8': '---.. ',
    '9': '---- ',
    ' ': '/ ',
}

def isalphanum(chaine):
    return all(char.isalnum() or char.isspace() for char in chaine )

def encode(string):
    res = ""
    for char in string:
        res += NESTED_MORSE[char]
    if res.endswith(" "):
        return res[:-1]
    return res

def main():
    try:
        assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
    except AssertionError as e:
        print(e)
        sys.exit(1)
    string = sys.argv[1]
    try:
        assert isalphanum(string), "AssertionError: the arguments are bad"
    except AssertionError as e:
        print(e)
        sys.exit(1)
    print(encode(string.upper()))


main()