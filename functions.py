import cv2
import numpy as np
import os
from scipy import ndimage

def highPassFiltering():
    kernel_3x3 = np.array([[-1, -1, -1],
                          [-1, 8, -1],
                          [-1, -1, -1]])
    kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                           [-1, 1, 2, 1, -1],
                           [-1, 2, -4, 2, 1],
                           [-1, 1, 2, 1, -1],
                           [-1, -1, -1, -1, -1]])

    img = cv2.imread("../../images/statue_small.jpg", 0)

    k3 = ndimage.convolve(img, kernel_3x3)
    k5 = ndimage.convolve(img, kernel_5x5)

    blurred = cv2.GaussianBlur(img, (17, 17), 0)

    g_hpf = img - blurred

    cv2.imshow("3x3", k3)
    cv2.imshow("5x5", k5)
    cv2.imshow("blurred", blurred)
    cv2.imshow("g_hpf", g_hpf)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cannyFiltering():
    img = cv2.imread("../../images/statue_small.jpg", 0)
    t_lower = int(input("Enter lower threshold: "))
    t_upper = int(input("Enter upper threshold: "))
    dst = cv2.Canny(img, t_lower, t_upper)
    cv2.imshow("Original", img)
    cv2.imshow("Canny Filtered", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def contour1():
    img = np.zeros((200, 200), dtype = np.uint8)
    img[50:150, 50:150] = 255

    ret, thresh = cv2.threshold(img, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
    cv2.imshow("contours", color)
    cv2.waitKey()
    cv2.destroyAllWindows()