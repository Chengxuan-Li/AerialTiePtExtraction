import os
from os.path import exists, join, basename, splitext
import numpy as np
import cv2
import matplotlib.pyplot as plt

YOUR_PATH = 'C:/Users/liche/PycharmProjects/AerialTiePtExtraction/'
os.system('cd {path}'.format(path=YOUR_PATH))
os.environ['PATH'] += ";{path}micmac/bin".format(path=YOUR_PATH)
print(os.environ['PATH'])


def Test():
    os.system('mm3d')