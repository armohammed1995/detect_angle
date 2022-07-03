import cv2
import math
########################################################################
path = 'angle.png'
img = cv2.imread( path)
mouse_points_list = []
########################################################################
def mouse_point (event,x,y,flags,prams):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y) ,10, (0,225,100, cv2.FILLED))
        mouse_points_list.append([x,y])
########################################################################
def gradient(pt1,pt2):
    grad = (pt2[1]-pt1[1]) / (pt2[0]-pt1[0])
    return grad
########################################################################
def angle(mouse_points_list):
    pt1, pt2, pt3  = mouse_points_list[-3:]
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1,pt3)
    angR = math.atan((m1-m2)/(1+(m1*m2)))
    ang_deg = round(math.degrees(angR))
    print(ang_deg)
########################################################################
while True:

    if len(mouse_points_list) %  3 == 0 and len(mouse_points_list) != 0:
        angle(mouse_points_list)
    cv2.imshow('image', img)
    cv2.setMouseCallback( 'image', mouse_point)

    if cv2.waitKey(1) &  0xff == ord('q'):
        mouse_points_list = []
        img = cv2.imread(path)

