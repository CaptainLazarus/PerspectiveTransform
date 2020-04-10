import cv2
import imutils
from lazarus.transform import *
from skimage.filters import threshold_local
import argparse
import imutils

def initArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i" , "--image" , required = True , help="Input image path")
    return vars(parser.parse_args())
    

if __name__ == "__main__":
    args = initArgs()
    image = cv2.imread(args["image"])
    # cv2.imshow("Image" , image)
    # cv2.waitKey()

    ratio = image.shape[0]/500
    orig = image.copy()


    image = imutils.resize(image , height = 500)
    
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gray" , gray)
    # cv2.waitKey(0)

    gray = cv2.GaussianBlur(gray , (5,5) , 0)
    # cv2.imshow("Gray" , gray)
    # cv2.waitKey(0)
    
    edge = cv2.Canny(gray , 100 , 200)

    # cv2.imshow("Image" , image)
    # cv2.imshow("Edges" , edge)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    c = cv2.findContours(edge.copy() , cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)
    c = imutils.grab_contours(c)

    c = sorted(c , key=cv2.contourArea , reverse=True)[:5]

    for k in c:
        peri = cv2.arcLength(k,True)
        approx = cv2.approxPolyDP(k , 0.02*peri , True)

        if len(approx)==4:
            screenC = approx
            break

    cv2.drawContours(image , [screenC] , -1 , (0,255,0) , 3)
    # cv2.imshow("Contours" , image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Done until here
    warped = four_point_transform(orig , screenC.reshape(4 , 2) * ratio)


    # Extra stuff -> Back and white -> Edges/ Blurring
    warped = cv2.cvtColor(warped , cv2.COLOR_BGR2GRAY)
    T = threshold_local(warped , 11 , offset=10 , method="gaussian")
    warped = (warped>T).astype("uint8") * 255

    # print(warped)
    cv2.imshow("Original" , orig)
    cv2.imshow("Warped" , warped)
    cv2.waitKey(0)