from skimage.io import imread

from .paths import PATH_H, PATH_E, PATH_NORM, PATH_GT


def load_case(img_id):
    imgH = imread(PATH_H / img_id)
    imgE = imread(PATH_E / img_id)
    imgN = imread(PATH_NORM / img_id)
    imgGT = imread(PATH_GT / img_id)
    return imgH, imgE, imgN, imgGT
