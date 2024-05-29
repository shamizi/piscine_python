class calculator:
#your code here
    def __init__(self, object) -> None:
        self.list = object

    def __add__(self, object) -> None:
        self.list = [x + object for x in self.list]
        print(self.list)
        return [x for x in self.list]
#your code here
    def __mul__(self, object) -> None:
        self.list = [x * object for x in self.list]
        print(self.list)
        return [x for x in self.list]

    def __sub__(self, object) -> None:
        self.list = [x - object for x in self.list]
        print(self.list)
        return [x for x in self.list]
    
    def __truediv__(self, object) -> None:
        try :
            if object == 0:
                raise AssertionError("can't divide by 0")
            self.list = [x / object for x in self.list]
            print(self.list)
            return [x for x in self.list]
        except AssertionError as e:
            print(e)
        


# v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# v1 + 5
# print("---")
# v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# v2 * 5
# print("---")
# v3 = calculator([10.0, 15.0, 20.0])
# v3 - 5
# v3 / 5
# v3 / 0
# v3 + 5