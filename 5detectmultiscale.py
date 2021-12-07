import cv2
face_cascade = cv2.CascadeClassifier('data\\xml\\haarcascade_frontalface_default.xml')
img = cv2.imread('data_testing//wajah.jpg', cv2.IMREAD_GRAYSCALE)
wajah = face_cascade.detectMultiScale(img, 1.1, 3)
if len(wajah) == True:
    print('yes')
else:
    print('no')
