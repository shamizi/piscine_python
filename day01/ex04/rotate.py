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
            print("The shape of image is", ret, "or", ret[0:2])
            res = np.array(newImage)
            print(res)
            return res
    except Exception as e:
        print(e)
        return None

def ft_rotate(image_array: np.ndarray) -> np.ndarray:
    if len(image_array.shape) == 3:
        h, w, c = image_array.shape
        rotated_image = np.zeros((w, h, c), dtype=image_array.dtype)
        for i in range(h):
            for j in range(w):
                rotated_image[w - 1 - j, i] = image_array[i, j]
    else:
        h, w = image_array.shape
        rotated_image = np.zeros((w, h), dtype=image_array.dtype)
        for i in range(h):
            for j in range(w):
                rotated_image[w - 1 - j, i] = image_array[i, j]
    print("New shape after Transpose:", rotated_image.shape)
    print(rotated_image)
    return rotated_image


def main():
    # print(ft_zoom("animal.jpeg"))
    # #ouverture de l'image si tu veux mais creer un warning donc decommente si tu veux

    # transpose = ft_rotate(Image.open("newimage.jpeg"))
    # transpose.show()
    zoomed_image = ft_zoom("animal.jpeg")
    if zoomed_image is not None:
        rotated_image = ft_rotate(zoomed_image)
        if rotated_image is not None:
            test = Image.open("newimage.jpeg")
            test.show()
            rotated_pil_image = Image.fromarray(rotated_image)
            rotated_pil_image.show()

if __name__ == "__main__":
    main()