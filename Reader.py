#Input: Path to the Image
#Output: Image

import cv2

class Reader:
    def __init__(self, path):
        self.path = path

    def getImage(self):
        return cv2.imread(self.path)
