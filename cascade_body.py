import cv2
face_cascade = cv2.CascadeClassifier('data\\xml\\haarcascade_fullbody.xml')
img = cv2.imread('data_testing//sasa.jpg', cv2.IMREAD_GRAYSCALE)
wajah = face_cascade.detectMultiScale(img, 1.1, 3)
if len(wajah) == True:
    print('yes')
else:
    print('no')
