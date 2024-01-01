import cv2

# 得到圖片編號
def serial_number(max_number = 50):
    
    count = 0

    while(count < max_number):
        
        image = cv2.imread("./camera_pc/saved_{}.jpg".format(count))

        # 檢查是否成功讀取
        if image is not None:
            count += 1
        else:
            print(f"Image saved as saved_{count}.jpg")
            return count
 
# 存圖片
def camera_capture(frame, width=[-1, -1], high=[-1, -1]):

    number = serial_number()
    
    if width[0] != -1:
        cv2.imwrite("./camera_pc/saved_{}.jpg".format(number), frame[high[0]:high[1], width[0]:width[1]])

    else:
        cv2.imwrite("./camera_pc/saved_{}.jpg".format(number), frame)


if __name__ == "__main__":

    # 開啟攝影機(cv2.VideoCapture(攝影機編號), 視窗大小640*480)
    cap = cv2.VideoCapture(0)

    # 擷取範圍
    cut_width=[200, 440]
    cut_high=[120, 360]
    line_width = 2

    while(True):

        # 讀取攝影機影像
        ret, frame = cap.read()

        # 繪製對齊框線 (X1 Y1, X2 Y2)
        cv2.rectangle(frame, (cut_width[0] - line_width, cut_high[0] - line_width), 
                             (cut_width[1] + line_width, cut_high[1] + line_width), 
                             (0, 255, 0) ,line_width)
    
        cv2.imshow("frame", frame)

        keyboard = cv2.waitKey(1)

        # 擷取視窗
        if keyboard == ord('c'):
            camera_capture(frame, cut_width, cut_high)

        # ESC ASCII code = 27
        if keyboard == 27:
            break
        
    cv2.destroyAllWindows()
    cap.release()