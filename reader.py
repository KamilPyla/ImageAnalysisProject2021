import cv2
import numpy as np
import matplotlib.pyplot as plt

class ReaderGrey:
  def __init__(self, file):
    self.image = cv2.imread(file, 0)
    
