# Input: Image
# Output:  Converted image

import cv2


# Idea: Firstly detect car and work at car image?
class Converter:
    def __init__(self, img):
        self.orginalImg = img
        self.copyImg = img.copy()
        # [0] -> height, [1] -> width, [2] -> channels
        self.dimensions = img.shape

    def showOriginal(self):
        cv2.imshow("Original Image", self.orginalImg)
        cv2.waitKey(0)

    def showCopy(self):
        cv2.imshow("Copy Status", self.copyImg)
        cv2.waitKey(0)

    def convertImage(self):
        self.copyImg = cv2.resize(self.copyImg, (1920, 1080), interpolation=cv2.INTER_AREA) # Test-only
        self.convertToGray(self.copyImg)
        self.removeNoise(self.copyImg)
        self.edgeDetection(self.copyImg)

    def scaleImg(self):
        (newWidth, newHeight) = 800, 600

    def convertToGray(self, img):
        isInGray = False
        isInRGB = False

        if len(img.shape)  == 2: 
            isInGray = True
        elif len(img.shape) == 3:
            isInRGB = True

        if isInRGB:
            self.copyImg = cv2.cvtColor(self.copyImg, cv2.COLOR_BGR2GRAY)

    # TO-DO: Finding best values
    def removeNoise(self, img): 
        # Diameter of each pixel neighborhood that is used during filtering. If it is non-positive, it is computed from sigmaSpace. 
        d = 9
        # Filter sigma in the color space. 
        # A larger value of the parameter means that farther colors within the pixel neighborhood (see sigmaSpace) 
        # will be mixed together, resulting in larger areas of semi-equal color. 
        sigmaColor = 75
        #Filter sigma in the coordinate space. 
        # A larger value of the parameter means that farther pixels will influence each other as 
        # long as their colors are close enough (see sigmaColor ). When d>0, it specifies the neighborhood size regardless of sigmaSpace. 
        # Otherwise, d is proportional to sigmaSpace. 
        sigmaSpace = 75
        cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace)

    # TO-DO: Finding best values
    def edgeDetection(self, img):
        # First threshold for the hysteresis procedure. 
        threshold1 = 30
        # Second threshold for the hysteresis procedure. 
        threshold2 = 200

        self.copyImg = cv2.Canny(img, threshold1, threshold2)
'''
import cv2

class Converter:
    def __init__(self, imgPath):
        self.image = cv2.imread(imgPath)
        self._convertImage(1360, 720) 

    def _convertImage(self, width, height):
        scaledImage = cv2.resize(self.image, (width, height))
        grayImage = cv2.cvtColor(scaledImage, cv2.COLOR_BGR2GRAY)
        self.image = grayImage 

    def _removeImperfections(self):
        
    # Testing purposes only
    def showImage(self):
        cv2.imshow('Actual image status', self.image)
        cv2.waitKey(0)
'''