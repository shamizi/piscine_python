from load_image import ft_load
import numpy as np
from PIL import Image
import sys


def ft_zoom(path: str) -> np.ndarray:
    try:
        print(ft_load(path))
        image = Image.open(path)
        if image is not None:
            newImage = image.crop((6,image.size[0] / 6, 174, 3 * image.size[0] / 4))
            newImage = newImage.resize((400, 400))
            newImage = newImage.convert("L")
            ret = (newImage.size[1], newImage.size[0], len(newImage.mode))
            newImage.save("newimage.jpeg")
            print("New shape after slicing:", ret, "or", ret[0:2])

            res = []
            for x in range(newImage.size[0]):
                column = []
                for y in range(newImage.size[1]):
                    column.append([newImage.getpixel((x, y))])
                res.append(column)
            return np.array(res)
    except Exception as e:
        print(e)
        return None

def main():
    print(ft_zoom("animal.jpeg"))
    #ouverture de l'image si tu veux mais creer un warning donc decommente si tu veux
    #test = Image.open("newimage.jpeg")
    #test.show()

if __name__ == "__main__":
    main()