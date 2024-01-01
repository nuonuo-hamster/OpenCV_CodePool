import numpy as np
import cv2

# 遮罩
def mask(hsv_img, hsv_lower, hsv_upper):
        
    # 二值化為純黑純白影像，若介於自定義顏色區間內令像素值為255，反之則令像素值為0
    img_thres = cv2.inRange(hsv_img, hsv_lower, hsv_upper)
    
    # 以二值化影像為遮罩，將原始影像進行邏輯閘and-gate運算 (cv2.bitwise_and(輸入影像1, 輸入影像2, 遮罩影像))
    img_masked = cv2.bitwise_and(img, img, None, mask=img_thres)

    return img_thres, img_masked

def countour_rect(img, hsv_thres):

    countour = img.copy()
    contact_rec =img.copy()
    min_contact_rec = img.copy()

    # 找輪廓
    (cnts, _) = cv2.findContours(hsv_thres.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 回傳輪廓list

    cv2.drawContours(countour, cnts, -1, (0, 255, 0), 2)

    for cnt in cnts:

        # 矩形 rect
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(contact_rec, (x, y), (x + w, y + h), (0, 0, 255), 1)
        
        # 最小外接矩形
        BoundingBox = cv2.minAreaRect(cnt)  # 最小外接矩形的中心（x，y），（寬度，高度），旋轉角度）
        BoundingBox = np.int0(cv2.boxPoints(BoundingBox))  # int0 會省略小數點後方的數字
        cv2.drawContours(min_contact_rec, [BoundingBox], -1, (0, 255, 0), 1)

    return countour, contact_rec, min_contact_rec


if __name__ == "__main__":

    img = cv2.imread('./image_mask/balls.jpg')
    img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110,125,84])
    upper_blue = np.array([122,255,200])

    # 遮罩
    img_thres, hsv_mask = mask(hsv_img, lower_blue, upper_blue)
    # 找輪廓 & 外接矩形
    countour, contact_rec, min_contact_rec = countour_rect(img, img_thres)


    image_h1 = cv2.hconcat([hsv_mask, countour]) # 遮罩 & 輪廓
    image_h2 = cv2.hconcat([contact_rec, min_contact_rec]) # 矩形 & 最小外接矩形
    result = cv2.vconcat([image_h1, image_h2])

    cv2.imshow('Contour', result) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()