import os
import cv2

if __name__ == "__main__":

    # 工作路徑
    path = os.getcwd()

    # file of Images
    file_list = os.listdir(path + '\\source_image')

    # add images into array
    images = []
    for img_name in file_list:

        img = cv2.imread(path + '\\source_image\\' + img_name)
        images.append(img)

    ### images = [cv2.imread(path + '\\source_image\\' + file) for file in file_list]

    # show
    print('amount of images:', len(images))
    for img in images:
        cv2.imshow("Image", img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()