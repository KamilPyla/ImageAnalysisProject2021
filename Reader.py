#Input: Path to the Image
#Output: Image
import os.path

import cv2


class Reader:
    def __init__(self, allowable_extensions):
        self.extensions = allowable_extensions
        self.image_readable = False

    def set_path(self, path):
        if os.path.exists(path) and os.path.isfile(path):
            if self.__validate_extension(path):
                self.image_readable = self.__try_to_open(path)

    def is_path_correct(self):
        return self.image_readable

    def get_image(self):
        return self.image

    def __validate_extension(self, path):
        is_correct = False

        for element in self.extensions:
            is_correct = path.endswith("." + element)

            if is_correct:
                break

        return is_correct

    def __try_to_open(self, path):
        try:
            self.image = cv2.imread(path)
            return True
        except OSError(path):
            print("Can't read the file!")
            return False
