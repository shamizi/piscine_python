from array2D import slice_me
family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
listvide = []
notalist = {1,2,3,4}
differentsize = [[1,2],
[1,2],
[1,2,3]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print(slice_me(family, -99, 100))
print(slice_me(listvide, -99, 100))
print(slice_me(family, "not an int", -2))
print(slice_me(notalist, 1, -2))
print(slice_me(differentsize, 1, -2))

