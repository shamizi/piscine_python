import sys

try:
    assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"
    if len(sys.argv) == 2:
        assert sys.argv[1].isdigit(), "AssertionError: argument is not an integer"
except AssertionError as msg:
    print(msg)
    sys.exit()
if len(sys.argv) == 2:
    if (int(sys.argv[1]) % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")