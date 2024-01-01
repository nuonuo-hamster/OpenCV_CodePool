import numpy as np
import cv2

# 建立滑桿函式
def hsv_track_bar(hsv_lower, hsv_upper, win_name):

    # 定義滑桿callback函式
    def on_trackbar_h_lower(value):
        hsv_lower[0] = min(value, hsv_upper[0]) # 1
    def on_trackbar_h_upper(value):
        hsv_upper[0] = max(value, hsv_lower[0]) # 2
    def on_trackbar_s_lower(value):
        hsv_lower[1] = min(value, hsv_upper[1]) # 3
    def on_trackbar_s_upper(value):
        hsv_upper[1] = max(value, hsv_lower[1]) # 4
    def on_trackbar_v_lower(value):
        hsv_lower[2] = min(value, hsv_upper[2]) # 5
    def on_trackbar_v_upper(value):
        hsv_upper[2] = max(value, hsv_lower[2]) # 6
    
    # 創建HSV上下界滑桿
    cv2.createTrackbar("H_lower\n", win_name, hsv_lower[0], 180, on_trackbar_h_lower)
    cv2.createTrackbar("H_upper\n", win_name, hsv_upper[0], 180, on_trackbar_h_upper)
    cv2.createTrackbar("S_lower\n", win_name, hsv_lower[1], 255, on_trackbar_s_lower)
    cv2.createTrackbar("S_upper\n", win_name, hsv_upper[1], 255, on_trackbar_s_upper)
    cv2.createTrackbar("V_lower\n", win_name, hsv_lower[2], 255, on_trackbar_v_lower)
    cv2.createTrackbar("V_upper\n", win_name, hsv_upper[2], 255, on_trackbar_v_upper)

# 更新滑桿  
def hsv_track_bar_update(hsv_lower, hsv_upper, win_name):
    
    cv2.setTrackbarPos("H_lower\n", win_name, hsv_lower[0])
    cv2.setTrackbarPos("H_upper\n", win_name, hsv_upper[0])
    cv2.setTrackbarPos("S_lower\n", win_name, hsv_lower[1])
    cv2.setTrackbarPos("S_upper\n", win_name, hsv_upper[1])
    cv2.setTrackbarPos("V_lower\n", win_name, hsv_lower[2])
    cv2.setTrackbarPos("V_upper\n", win_name, hsv_upper[2])

# 遮罩
def mask(img_hsv, hsv_lower, hsv_upper):
        
        # 二值化為純黑純白影像，若介於自定義顏色區間內令像素值為255，反之則令像素值為0
        img_thres = cv2.inRange(img_hsv, hsv_lower, hsv_upper)
        
        # 以二值化影像為遮罩，將原始影像進行邏輯閘and-gate運算 (cv2.bitwise_and(輸入影像1, 輸入影像2, 遮罩影像))
        img_masked = cv2.bitwise_and(img, img, mask=img_thres)

        return img_masked
    
if __name__ == "__main__":

    # 視窗
    win_name = 'HSV_Trackbar'
    cv2.namedWindow(win_name, cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow(win_name, 640, 480)

    # hsv 色相、飽和度、明度
    img = cv2.imread('./source_image/live_1.jpg')
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hsv_lower = np.array([100, 43, 46])
    hsv_upper = np.array([124, 255, 255])

    # 建立滑桿
    hsv_track_bar(hsv_lower, hsv_upper, win_name)

    while True:
        # 同步滑桿數值
        hsv_track_bar_update(hsv_lower, hsv_upper, win_name)
        
        img_masked = mask(img_hsv, hsv_lower, hsv_upper)
        
        image = cv2.hconcat([img, img_masked])   
        
        cv2.imshow(win_name, image)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
