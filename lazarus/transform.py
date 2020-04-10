import cv2
import numpy as np

def order_points(pts) -> list:
    rect = np.zeros((4,2) , dtype="float32")

    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    d = np.diff(pts , axis=1)
    rect[1] = pts[np.argmin(d)]
    rect[3] = pts[np.argmax(d)]

    return rect

def four_point_transform(image , pts):
    rect = order_points(pts)
    (tl , tr , br , bl) = rect

    # Max distance calculation
    A = np.sqrt( ((bl[0] - br[0])**2) + ((bl[1]-br[1])**2))
    B = np.sqrt( ((tl[0] - tr[0]) **2) + ((tl[1] - tr[1])**2) )
    maxw = max(int(A) , int(B))

    # print("A: {} \tB: {}\tmaxw: {}".format(A,B,maxw))

    # Max Height Calc
    C = np.sqrt(((bl[0]-tl[0])**2) + ((bl[1]-tl[1])**2))
    D = np.sqrt(((tr[0]-br[0])**2) + ((tr[1]-br[1])**2))
    maxh = max(int(C) , int(D))

    # print("C: {} \tD: {}\tmaxh: {}".format(A,B,maxh))

    dst = np.array([
        [0,0] , 
        [maxw-1 , 0],
        [maxw-1 , maxh-1],
        [0,maxh-1]
    ] , dtype="float32")

    M = cv2.getPerspectiveTransform(rect,dst)
    # print(M)
    warped = cv2.warpPerspective(image , M , (maxw , maxh))

    return warped

def _initArgs():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i" , "--image" , required=True , help="Input Image")
    parser.add_argument("-c" , "--coords" , help="Coordinates of vertices.")
    args = vars(parser.parse_args())
    return args

if __name__ == "__main__":
    print("This file is only for testing. DON'T run directly. Import it and use four_point_transform.")
    args = _initArgs()

    image = cv2.imread(args["image"])
    pts = np.array(eval(args["coords"]) , dtype="float32")

    warped = four_point_transform(image , pts)
    cv2.imshow("Original" , image)
    cv2.imshow("Warped" , warped)
    cv2.waitKey(0)