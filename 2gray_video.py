import cv2
nama = 'gray'

capture = cv2.VideoCapture(0)
while True:
    ret, img = capture.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow(nama, gray)
    keyCode = cv2.waitKey(1)
    if cv2.getWindowProperty(nama, cv2.WND_PROP_VISIBLE) < 1:
        break
