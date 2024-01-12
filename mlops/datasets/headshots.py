import cv2

name = 'Aymen'  
stream_url = 'http://192.168.137.192:4747/video' 

cap = cv2.VideoCapture(stream_url)
img_counter = 0

while True:
    ret, image = cap.read()
    if not ret:
        break
    cv2.imshow("Press Space to take a photo", image)

    k = cv2.waitKey(1)
    if k % 256 == 27:  # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:  # SPACE pressed
        img_name = "dataset/" + name + "/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, image)
        print("{} written!".format(img_name))
        img_counter += 1

cap.release()
cv2.destroyAllWindows()
