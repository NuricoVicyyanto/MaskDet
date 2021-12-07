import cv2
import winsound

title = 'experiment'
cascade = cv2.CascadeClassifier('data\\xml\\haarcascade_upperbody.xml')
cap = cv2.VideoCapture('data_testing\\cctv.mp4')


while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objeck = cascade.detectMultiScale(gray, 1.1, 3)

    if len(objeck) == True:
        for (x, y, w, h) in objeck:
            cv2.rectangle(img, (x, y), (x+ w, y+h), (0, 255, 0), 2)
            cv2.putText(img, "ada", (30, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow(title ,img)

    keyCode = cv2.waitKey(1)
    if cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) < 1:
        break