import cv2 as cv
import numpy as np
import apriltag
from tag_position import tag_positions


def tag_detect(img):
    # 创建detector对象
    options = apriltag.DetectorOptions(families='tag36h11',)
    detector = apriltag.Detector(options)
    gray = cv.cvtcolor(img,cv.COLOR_BGR2GRAY)
    tags = detector.detect(gray)
    tag_num = len(tags)
    for n, tag in enumerate(tags):
        pos = tag_positions[str(tag.id)]
        corners = np.array(tag.corners)
        