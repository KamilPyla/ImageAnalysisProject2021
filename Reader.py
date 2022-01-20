# Input: Path to the Image
# Output: Image

import os.path
import cv2


class Reader:
    """
    A class responsible for validating path and reading image.

    Attributes
    ----------
    extensions: List[str]
        a list of string with allowable file extension e.g. [".jpg", ".jpeg"]
    image_readable: Boolean
        if the file meets the assumptions
    image: image
        if everything is correct it contains image

    Public methods
    --------------
    set_path(path)
        Sets path to the file and validate it. If everything is correct reads the image.
    is_path_correct()
        If the file was successfully read return true, otherwise return false.
    get_image()
        Returning the read image. USe only after checking that path is correct.

    Private methods
    ---------------
     __validate_extension(path)
        Using extensions list validates the file.
     __try_to_open(path)
        Reading the file.
    """
    def __init__(self, allowable_extensions):
        """
        Parameters
        ----------
        allowable_extensions: List[str]
            a list of string with allowable file extension e.g. [".jpg", ".jpeg"]
        """
        self.extensions = allowable_extensions
        self.image_readable = False

    def set_path(self, path):
        """
        Parameters
        ----------
        path: str
             a path to the file
        """
        if os.path.exists(path) and os.path.isfile(path):
            if self.__validate_extension(path):
                self.image_readable = self.__try_to_open(path)

    def is_path_correct(self):
        """
        Returns
        --------
        image_readable: Boolean
            a value that indicates if image is readable
        """
        return self.image_readable

    def get_image(self):
        """
        Returns
        ----------
        image: image
            a read image
        """
        return self.image

    def __validate_extension(self, path):
        """
        Parameters
        ----------
        path: str
            a path to the file

        Returns
        ----------
        is_correct: Boolean
             an extension correctness
        """
        is_correct = False

        for element in self.extensions:
            is_correct = path.endswith("." + element)

            if is_correct:
                break

        return is_correct

    def __try_to_open(self, path):
        """
        Parameters
        ----------
        path: str
            a path to the file

        Raises
        ------
        OSError: path
            If the image couldn't be read

        Returns
        ----------
        Boolean
            if the image was read properly
        """
        try:
            self.image = cv2.imread(path)
            return True
        except OSError(path):
            print("Can't read the file!")
            return False
