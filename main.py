from os import path, read
from Converter import Converter
from Reader import Reader
from cv2 import cv2

if __name__ == "__main__":
    EXAMPLES_NUMBER = 9
    EXAMPLES_PATH = "example-img"
    pathList = []

    for i in range(EXAMPLES_NUMBER):
        pathList.append(EXAMPLES_PATH + "/Sample-" + str(i + 1) + ".jpg");

    
    for i in range(EXAMPLES_NUMBER):
        reader = Reader(pathList[i])
        converter = Converter(reader.getImage())

        '''
        converter.convertToGray(converter.copyImg)
        converter.showCopy()
        converter.removeNoise(converter.copyImg)
        converter.showCopy()
        '''

        converter.convertImage()
        converter.showCopy()
    

    '''
    reader = Reader(pathList[i])
    converter = Converter(reader.getImage())

    converter.convertImage()
    converter.showCopy()
    '''