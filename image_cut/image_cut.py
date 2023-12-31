import cv2

if __name__ == "__main__":

    img = cv2.imread(".\\source_image\\live_1.jpg")

    # 顯示影像資訊（寬、高、維度)
    print("Shape of Color Image: {}".format(img.shape))

    # 像素索引值 = (X, Y)
    idx_tl = (100, 100) # 左上角
    idx_br = (200, 300) # 右下角

    # X:X Y:Y
    img_roi = img[idx_tl[0]:idx_br[0], idx_tl[1]:idx_br[1]]

    # cv2.imwrite(".\\image_resize\\saved_img.jpg", img_zoomin)

    cv2.imshow('ROI Image', img_roi)

    cv2.waitKey(0)
    cv2.destroyAllWindows()