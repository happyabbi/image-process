# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# -*- coding: utf-8 -*-


# C:\Users\AbrahamCHen\PycharmProjects\ImageProcess\venv\Scripts\activate.bat
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org Image

import cv2
import imutils


def resize_cv():
    imageName = 41
    s = fr"C:\Users\AbrahamCHen\Downloads\image\{imageName}.jpg"

    img = cv2.imread(s)

    img_big = imutils.resize(img, width=3200)
    img_small = imutils.resize(img, width=1600)
    # rotation
    rotation_big_image = imutils.rotate_bound(img_big, 0)
    rotation_90_image = imutils.rotate_bound(img_small, 90)
    rotation_180_image = imutils.rotate_bound(img_small, 180)
    rotation_270_image = imutils.rotate_bound(img_small, 270)
    rotation_360_image = imutils.rotate_bound(img_small, 360)

    cv2.imwrite(fr'{imageName}_big.jpg', rotation_big_image)
    cv2.imwrite(fr'{imageName}_90.jpg', rotation_90_image)
    cv2.imwrite(fr'{imageName}_180.jpg', rotation_180_image)
    cv2.imwrite(fr'{imageName}_270.jpg', rotation_270_image)
    cv2.imwrite(fr'{imageName}_360.jpg', rotation_360_image)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    resize_cv()
    # resize()
    # resize_thumbnail()
    # auto_crop()
