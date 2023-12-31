import cv2

if __name__ == "__main__":

    img = cv2.imread(".\\source_image\\live_1.jpg")

    # 顯示影像資訊（寬、高、維度)
    print("Shape of Color Image: {}".format(img.shape))

    # 影像放大（寬, 高）
    img_zoomin = cv2.resize(img, (660, 512), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("ZoomIn Image", img_zoomin)

    # 影像縮小
    img_zoomout = cv2.resize(img, (165, 128), interpolation=cv2.INTER_AREA)
    cv2.imshow('ZoomOut Image', img_zoomout)

    # cv2.imwrite(".\\image_resize\\saved_img.jpg", img_zoomin)

    cv2.waitKey(0)
    cv2.destroyAllWindows()