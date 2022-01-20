from os import path, read
from Converter import Converter
from Reader import Reader
from cv2 import cv2

'''
if __name__ == "__main__":
    EXAMPLES_NUMBER = 9
    EXAMPLES_PATH = "example-img/"
    path_list = []
    image_list = []
    extensions = ["jpg", "jpeg", "png"]

    for i in range(EXAMPLES_NUMBER):
        path_list.append(EXAMPLES_PATH + "Sample-" + str(i + 1) + ".jpg")

    # list with images
    reader = Reader(extensions)

    # Reading images
    for i in range(EXAMPLES_NUMBER):
        reader.set_path(path_list[i])
        if reader.is_path_correct():
            image_list.append(reader.get_image())

    for i in range(EXAMPLES_NUMBER):
        converter = Converter(image_list[i])
        converter.convert_image()
        converter.show_copy()
'''