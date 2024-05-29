class calculator:

# decorator
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = sum(x * y for x, y in zip(V1, V2))
        print("Dot product is :", res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = [float(x + y) for x, y in zip(V1, V2)]
        print("Add Vector is :", res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is :", res)


# a = [5, 10, 2]
# b = [2, 4, 3]
# calculator.dotproduct(a,b)
# calculator.add_vec(a,b)
# calculator.sous_vec(a,b)
