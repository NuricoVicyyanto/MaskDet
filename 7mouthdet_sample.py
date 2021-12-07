import cv2
import winsound
#from controller.controller import *

face_cascade = cv2.CascadeClassifier('data\\xml\\cascade_face.xml')
mouth_cascade = cv2.CascadeClassifier('data\\xml\\haarcascade_mcs_mouth.xml')

count = 0

# Cahaya
threshold = 80

# Pesan teks
font = cv2.FONT_HERSHEY_DUPLEX #memanggil font opencv
org = (30, 30)
warna_font_pakai_masker = (255, 255, 255)
warna_font_tidak_pakai_masker = (0, 0, 255)
ketebalan = 2
ukuran_font = 1
title = "Pendeteksi Masker"

# mengambil video menggunakan webcam
capture =   cv2.VideoCapture(0)

while True:
    ret, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, black_and_white) = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    wajah = face_cascade.detectMultiScale(gray, 1.1, 3)
    wajah_hitam_putih = face_cascade.detectMultiScale(black_and_white, 1.1, 3)

    if(len(wajah) == False and len(wajah_hitam_putih) == False):
        cv2.putText(img, ".", org, font, ukuran_font, warna_font_pakai_masker, ketebalan, cv2.LINE_AA)
    else:
        # tanda persegi di wajah
        for (x, y, w, h) in wajah:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            
            mulut = mouth_cascade.detectMultiScale(gray, 1.1, 3)

        if(len(mulut) == False):
            cv2.putText(img, '.', org, font, ukuran_font, warna_font_pakai_masker, ketebalan, cv2.LINE_AA)
        else:
            for (mx, my, mw, mh) in mulut:
                if(y < my < y + h):
                    cv2.rectangle(img, (mx, my), (mx + mh, my + mw), (0, 0, 255), 3)

    # fungsi menampilkan dan exit
    cv2.imshow(title, img)
    keyCode = cv2.waitKey(1)
    if cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) < 1:
        break

# exit
capture.release()
cv2.destroyAllWindows()