# program to capture the background image and save it

import cv2

# capture video from the webcam
cap = cv2.VideoCapture(0)

# while webcam exits/opened
while cap.isOpened():

    # read frame by frame
    success, back = cap.read()

    # if image was read
    if success:
        # display the image
        cv2.imshow("Image", back)
        # if q is pressed between 5 ms of any frame(wait time) then save the image and break out of loop
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite("bgimage.jpg", back)
            break

# release the captured video
cap.release()
# destroy all windows
cv2.destroyAllWindows()

