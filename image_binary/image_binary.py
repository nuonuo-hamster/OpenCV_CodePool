import cv2

if __name__ == "__main__":

    img = cv2.imread(".\\source_image\\live_1.jpg")
    img = cv2.resize(img, (480, 360), interpolation=cv2.INTER_AREA)
    
    # 灰階化
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 參數設定（門檻值, 像素值上限, 模式）

    # 比閾值黑的黑，比閾值白的白
    ret, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

    # 比閾值黑的白，比閾值白的黑
    ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

    # 比閾值黑的不變，比閾值白的閾值
    ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)

    # 比閾值黑的黑，比閾值白的不變
    ret, thresh4 = cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO)


    image_h1 = cv2.hconcat([img_gray, thresh1, thresh2])
    image_h2 = cv2.hconcat([img_gray, thresh3, thresh4])

    result_img = cv2.vconcat([image_h1, image_h2])
    
    # cv2.imwrite(".\\image_binary\\saved_img.jpg", result)

    cv2.imshow('result', result_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()