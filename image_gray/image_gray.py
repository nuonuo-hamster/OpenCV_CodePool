import cv2

if __name__ == "__main__":

    img = cv2.imread(".\\source_image\\live_1.jpg")

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(".\\gray_image\\saved_img.jpg", img_gray)
    cv2.imshow("Image", img_gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()