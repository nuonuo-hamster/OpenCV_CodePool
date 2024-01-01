import cv2

# 检查是否打开正确
def VideoIsOpened(vc):
   
    if vc.isOpened():
        open = True
        # open, frame = vc.read()
        return open
    else:
        open = False
        print('Video Is Opened:',open)
        return open

if __name__ == "__main__":

    vc = cv2.VideoCapture('.\\video_read\\test.mp4')

    open = VideoIsOpened(vc)

    delay = 10

    while (open):

        ret, frame = vc.read()

        if frame is None:
            break

        if ret == True:
            
            gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)
            cv2.imshow('result', gray)

            if cv2.waitKey(delay) == 27: #esc
                break

    cv2.destroyAllWindows()
    vc.release()