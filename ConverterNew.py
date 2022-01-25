import cv2


class ConverterNew:

    def convert_photo(self, img):
        img = self.__convert_to_gray(img)
        img = self.__remove_noise_and_prepare(img)
        img = self.__detect_edges(img)

        return img

    def __convert_to_gray(self, img):
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return img

    def __remove_noise_and_prepare(self, img):
        img = cv2.bilateralFilter(img, 9, 75, 75)
        se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
        bg = cv2.morphologyEx(img, cv2.MORPH_DILATE, se)
        img = cv2.divide(img, bg, scale=255)

        return img

    def __detect_edges(self, img):
        #img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1]
        img = cv2.Canny(img, 30, 200)

        return img