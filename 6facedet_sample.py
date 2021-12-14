import cv2

face_cascade = cv2.CascadeClassifier('data\\xml\\cascade_face.xml')


nama = 'gray'

capture = cv2.VideoCapture(0)
while True:
    ret, img = capture.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, black_and_white) = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)
    wajah = face_cascade.detectMultiScale(gray, 1.1, 3)

    if len(wajah)== True:
        for (x, y, w, h) in wajah:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
    else:
        pass


    cv2.imshow(nama, img)
    keyCode = cv2.waitKey(1)
    if cv2.getWindowProperty(nama, cv2.WND_PROP_VISIBLE) < 1:
        break
