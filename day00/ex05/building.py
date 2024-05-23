import sys

def maj_count(object: any) ->int:
    count = 0
    for letter in object:
        if letter.isupper():
            count += 1
    return count

def min_count(object: any) ->int:
    count = 0
    for letter in object:
        if letter.islower():
            count += 1
    return count

def space_count(object: any) ->int:
    count = 0
    for letter in object:
        if letter.isspace():
            count += 1
    return count

def digit_count(object: any) ->int:
    count = 0
    for letter in object:
        if letter.isdigit():
            count += 1
    return count

def punct_count(object: any) ->int:
    ponctuations = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
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
    returns : c'la les nombres
    """
    try:
        assert len(sys.argv) == 2, "usage 2 argument"
    except AssertionError as e:
        print(e)
        sys.exit(1)
    string = sys.argv[1]
    print("nombre de majuscule:", maj_count(string))
    print("nombre de minuscule:", min_count(string))
    print("nombre de digit:", digit_count(string))
    print("nombre de punct:", punct_count(string))
    print("nombre de whitespace:", space_count(string))
    print("la chaine contient", len(string), "caractere")
    print("la doc\n", main.__doc__)
main()