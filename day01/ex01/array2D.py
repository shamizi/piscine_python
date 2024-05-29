import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list) or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Format : list, int, int")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("List with different size")
        print("My shape is :", np.asarray(family).shape)
        x = slice(start, end)
        ret = family[x]
        print("My new shape is :", np.asarray(ret).shape)
        return ret
    except AssertionError as e:
        print(e)
        return