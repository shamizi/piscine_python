from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    try:
        if not path.endswith(("jpg", "jpeg")):
            raise AssertionError("jpg or jpeg format only")
        image = Image.open(path)
        if image is not None:
            ret = (image.size[1], image.size[0], len(image.mode))
            print("The shape of image is:", ret)
            #return list(image.getdata())
            return np.array(image)
    except Exception as e:
        print("Couldn't open image because :", e)
        return None