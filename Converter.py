# Input: Image
# Output:  Converted image

import cv2


class Converter:
    """
    A class that converts image to form allowing to detect license plate.

    Attributes
    ----------
    original_image : image
        an original image
    copy_image : image
        a copy of the original image to perform operations
    dimensions : List
        a dimensions of the image => [0] -> height, [1] -> width, [2] -> channels

    Methods
    -------
    convert_image()
        Converts an image to the form where license plates text and edges are well visible.
    __convert_to_gray(img)
    __remove_noise_and_prepare(img)
    __edge_detection(img)
    """
    def __init__(self, img):
        """
        Parameters
        ----------
        img: Image
            an image of car with license plate
        """
        self.original_image = img
        self.copy_image = img.copy()
        # [0] -> height, [1] -> width, [2] -> channels
        self.dimensions = img.shape

    def convert_image(self):
        self.__convert_to_gray(self.copy_image)
        self.__remove_noise_and_prepare(self.copy_image)
        self.__edge_detection(self.copy_image)

    def __convert_to_gray(self, img):
        """
        Parameters
        ----------
        img: Image
            an image of car with license plate
        """
        is_gray = False
        is_rgb = False

        if len(img.shape) == 2:
            is_in_gray = True
        elif len(img.shape) == 3:
            is_in_rgb = True

        if is_in_rgb:
            self.copy_image = cv2.cvtColor(self.copy_image, cv2.COLOR_BGR2GRAY)

    def __remove_noise_and_prepare(self, img):
        """
        Parameters
        ----------
        img: Image
            a gray image of car with license plate
        """
        img = cv2.bilateralFilter(img, 9, 75, 75)
        se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
        bg = cv2.morphologyEx(self.copy_image, cv2.MORPH_DILATE, se)
        self.copy_image = cv2.divide(self.copy_image, bg, scale=255)

    def __edge_detection(self, img):
        """
        Parameters
        ----------
        img: Image
            a gray and preprocessed image of car with license plate
        """
        # Better text at license plates
        self.copy_image = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1]
        # Better contours
        self.copy_image = cv2.Canny(self.copy_image, 30, 200)