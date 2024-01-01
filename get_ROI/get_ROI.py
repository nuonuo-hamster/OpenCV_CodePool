import cv2

if __name__ == "__main__":

    img = cv2.imread(".\\source_image\\live_1.jpg")

    # 滑鼠框選區域 (x, y, w, h)
    select_data = cv2.selectROI('ROI selector',img)

    x,y,w,h = select_data

    img_choose = img[y : y+h, x : x+w]

    print('X:{}\nY:{}\nW:{}\nH:{}'.format(x,y,w,h))

    if x*y*w*h != 0:
        cv2.imwrite(".\\get_ROI\\saved_img.jpg", img_choose)
    else:
        print('invalid')
