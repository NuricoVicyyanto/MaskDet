import cv2
nama = 'hitam putih'

capture = cv2.VideoCapture(0)
while True:
    ret, img = capture.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, black_and_white) = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)
    cv2.imshow(nama, black_and_white)
    keyCode = cv2.waitKey(1)
    if cv2.getWindowProperty(nama, cv2.WND_PROP_VISIBLE) < 1:
        break
