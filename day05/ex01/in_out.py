def square(x: int | float) -> int | float:
    return x * x

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:
        nonlocal x
        res = function(x)
        x = res
        return res
    return inner    

my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
