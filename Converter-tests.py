# Input: Image
# Output:  Converted image

import cv2
import numpy


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
        Prints the animals name and what sound it makes
    """
    def __init__(self, img):
        self.original_image = img
        self.copy_image = img.copy()
        # [0] -> height, [1] -> width, [2] -> channels
        self.dimensions = img.shape

    '''
    def show_original(self):
        cv2.imshow("Original Image", self.original_image)
        cv2.waitKey(0)

    def show_copy(self):
        cv2.imshow("Copy Status", self.copy_image)
        cv2.waitKey(0)
    '''

    def convert_image(self):
        #self.copy_image = cv2.resize(self.copy_image, (1920, 1080), interpolation=cv2.INTER_AREA) # Test-only
        #self.scale_image(800, 600)
        self.convert_to_gray(self.copy_image)
        self.remove_noise(self.copy_image, 9, 75, 75)
        self.edge_detection(self.copy_image, 30, 200)

        '''
        # ~ 5s - time
        self.copy_image = cv2.fastNlMeansDenoisingColored(self.copy_image, None, 10, 10, 7, 21)
        self.increase_details()

        #b, g, r = cv2.split(self.copy_image)
        #self.copy_image = b
        self.tests()
        #self.copy_image = cv2.adaptiveThreshold(self.copy_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        #self.copy_image = cv2.adaptiveThreshold(self.copy_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        #ret3, self.copy_image = cv2.threshold(self.copy_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        '''

    def scale_image(self, x, y):
        # (newWidth, newHeight) = 800, 600
        self.copy_image = cv2.resize(self.copy_image, (x, y), interpolation=cv2.INTER_AREA)

    def increase_details(self):
        #self.copy_image = cv2.detailEnhance(self.copy_image, 10, 0.15)
        self.copy_image = cv2.detailEnhance(self.copy_image, 100, 0.15)

    def tests(self):
        self.convert_to_gray(self.copy_image)
        sharpen_kernel = numpy.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        test_kernel = numpy.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        #self.copy_image = cv2.filter2D(self.copy_image, -1, test_kernel)
        #self.copy_image = cv2.GaussianBlur(self.copy_image, (3, 3), 0)
        self.copy_image = cv2.pyrUp(self.copy_image)
        self.copy_image = cv2.pyrUp(self.copy_image)
        self.copy_image = cv2.pyrUp(self.copy_image)
        #self.copy_image = cv2.filter2D(self.copy_image, -1, test_kernel)
        #self.copy_image = cv2.filter2D(self.copy_image, -1, test_kernel)
        #self.copy_image = cv2.filter2D(self.copy_image, -1, test_kernel)
        self.copy_image = cv2.filter2D(self.copy_image, -1, test_kernel)
        #self.copy_image = cv2.filter2D(self.copy_image, -1, test_kernel)
        self.remove_noise(self.copy_image, 9, 75, 75)
        self.remove_noise(self.copy_image, 9, 75, 75)
        self.remove_noise(self.copy_image, 9, 75, 75)
        self.edge_detection(self.copy_image, 1, 100)

        #self.scale_image(1360, 720)

    def convert_to_gray(self, img):
        is_in_gray = False
        is_in_rgb = False

        if len(img.shape) == 2:
            is_in_gray = True
        elif len(img.shape) == 3:
            is_in_rgb = True

        if is_in_rgb:
            self.copy_image = cv2.cvtColor(self.copy_image, cv2.COLOR_BGR2GRAY)

    # TO-DO: Finding best values
    def remove_noise(self, img, d, sigmaColor, sigmaSpace):
        # Diameter of each pixel neighborhood that is used during filtering. If it is non-positive, it is computed from sigmaSpace. 
        # d = 9
        # Filter sigma in the color space. 
        # A larger value of the parameter means that farther colors within the pixel neighborhood (see sigmaSpace) 
        # will be mixed together, resulting in larger areas of semi-equal color. 
        # sigmaColor = 75
        #Filter sigma in the coordinate space. 
        # A larger value of the parameter means that farther pixels will influence each other as 
        # long as their colors are close enough (see sigmaColor ). When d>0, it specifies the neighborhood size regardless of sigmaSpace. 
        # Otherwise, d is proportional to sigmaSpace. 
        # sigmaSpace = 75
        cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace)

    # TO-DO: Finding best values
    def edge_detection(self, img, f_threshold, s_threshold):
        # First threshold for the hysteresis procedure. 
        # threshold1 = 30
        # Second threshold for the hysteresis procedure. 
        # threshold2 = 200

        self.copy_image = cv2.Canny(img, f_threshold, s_threshold)