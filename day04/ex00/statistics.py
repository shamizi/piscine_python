def ft_statistics(*args: any, **kwargs: any) -> None:
   # allow_key = {"mean", "median", "quartile", "std", "var"}
    length = 0
    numbers = []
    quartile = []
    for arg in args:
        if not isinstance(arg, int):
            raise ValueError("ERROR not a number")
        numbers.append(arg)
        length += 1
    numbers.sort()
    #print("numbers :", numbers)
    for key, value in kwargs.items():
        if length == 0:
            print("ERROR")
        elif value == "mean":
            print("mean :", sum(args) / length)
        elif value == "median":
            if (length % 2 == 1):
                print("median :", numbers[length // 2])
            else :
                print("median :", (numbers[(length // 2) -1] + numbers[length // 2]) / 2)
        elif value == "quartile":
            quartile.append(float(numbers[((length+1) // 4)]))
            quartile.append(float(numbers[(3 * (length + 1) // 4) -1] ))
            print("quartile :", quartile)
        elif value == "std":
            moy = sum(args) / length
            ecart_carre = sum((x - moy) ** 2 for x in numbers)
            res = (ecart_carre / length) ** 0.5
            print("std :", res)
        elif value == "var":
            moy = sum(args) / length
            ecart_carre = sum((x - moy) ** 2 for x in numbers)
            res = ecart_carre / length
            print("var :", res)



try:
    ft_statistics(1, 42, 360, 11, 64,  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    print("a partir de la c des test perso")
    ft_statistics(1, 2, 3, 4, 'z', toto="mean", tutu="median", tata="quartile")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
except ValueError or AssertionError as e:
    print(e)