#載入套件
import numpy as np
import cv2
from matplotlib import pyplot as plt

#定義LBP演算法的函數
def lbp(img):
    assert(len(img.shape) == 2) # LBP只接受灰階影像
    ret = np.zeros_like(img)
    
    # 將圖片擴大，為了可以處理邊界
    img = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
    
    for y in range(1, img.shape[0] - 1):
        for x in range(1, img.shape[1] - 1):
            center = img[y][x]
            pixel = 0
            pixel |= (img[y - 1][x - 1] >= center) << 0
            pixel |= (img[y - 1][x + 0] >= center) << 1
            pixel |= (img[y - 1][x + 1] >= center) << 2
            pixel |= (img[y + 0][x + 1] >= center) << 3
            pixel |= (img[y + 1][x + 1] >= center) << 4
            pixel |= (img[y + 1][x + 0] >= center) << 5
            pixel |= (img[y + 1][x - 1] >= center) << 6
            pixel |= (img[y + 0][x - 1] >= center) << 7
            
            ret[y-1][x-1] = pixel
    return ret

#自訂一個秀圖片的函數
def showImage(image):
    '''
    在jupyter中使用matplotlib直接顯示圖片在記事本中
    '''
    # OpenCV的彩色影像 需轉成RGB順序
    if len(image.shape) == 3 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
    # OpenCV的灰階影像 需要特別調整 plt.imshow 的參數
    if len(image.shape) == 2:
        plt.imshow(image, cmap=plt.cm.gray, vmin=0, vmax=255)
    plt.show()
            
if __name__ == "__main__":
            
    #讀取圖片
    img = cv2.imread('./source_image/live_1.jpg')

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 將影像轉為灰階
    showImage(img)
    print(img.shape)

    lbp_img = lbp(gray_img)
    showImage(lbp_img)
    print(lbp_img.shape)
    
    cv2.imwrite(".\\image_lbp\\saved_img.jpg", lbp_img)