#!/usr/bin/env python
# -*-coding:utf-8-*-
import cv2
import os
# Load an color image in grayscale

def rewrite_size(file_name):
    img = cv2.imread('E:/log/src/'+ file_name ,3)
    res=cv2.resize(img,(1340,1104),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('E:/log/rewrite_src/'+ file_name,res)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def get_files():
    path = "E:/log/src/"
    for root, dirs, files in os.walk(path):
        for file_name in files:
            rewrite_size(file_name)
        # print(files)


if __name__ == '__main__':
    get_files()
