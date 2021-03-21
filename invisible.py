import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
# load background image
back = cv2.imread("./bgimage.jpg")

while cap.isOpened():
    success, frame = cap.read()

    if success:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv image", hsv)

        # getting the hsv code for red color from bgr code
        red = np.uint8([[[0,0,255]]])
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

        # threshold values for red color
        lower_red = np.array([0,100,100])
        upper_red = np.array([10,255,255])

        # to show only red color that falls in specified range
        mask = cv2.inRange(hsv, lower_red, upper_red)

        # connecting/masking the background
        part1 = cv2.bitwise_and(back, back, mask=mask)

        # getting colors that are not red
        mask = cv2.bitwise_not(mask)

        # getting the live frame
        part2 = cv2.bitwise_and(frame, frame, mask=mask)

        # showing the two added frames (red color will get invisible and rest will be shown)
        cv2.imshow("cloak", part1 + part2)

        if cv2.waitKey(5) == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()