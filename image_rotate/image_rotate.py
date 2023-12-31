import cv2

# 定义旋转rotate函数
def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]
 
    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)
 
    # 执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
 
    # 返回旋转后的图像
    return rotated

if __name__ == "__main__":

    img = cv2.imread(".\\source_image\\live_1.jpg")

    image_30 = rotate(img, 30, center=None, scale=1.0)

    image_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    image_180 = cv2.rotate(img, cv2.ROTATE_180)

    image_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    #  0 表示垂直翻轉
    image_vertical = cv2.flip(img, 0)
    #  1 表示水平翻轉
    image_horizontal = cv2.flip(img, 1)
    # -1 表示同時進行水平和垂直翻轉
    image_both = cv2.flip(img, -1)

    image_h1 = cv2.hconcat([image_30, image_180])
    image_h2 = cv2.hconcat([image_vertical, image_horizontal])
    
    result1 = cv2.vconcat([image_h1, image_h2])
    result2 = cv2.hconcat([image_90, image_270])

    cv2.imwrite(".\\image_rotate\\saved_img.jpg", result1)
    
    cv2.imshow("Image1", result1)
    cv2.imshow("Image2", result2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()