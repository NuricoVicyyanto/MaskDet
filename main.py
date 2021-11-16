import cv2
import winsound
from controller.controller import *

face_cascade = cv2.CascadeClassifier('data\\xml\\haarcascade_frontalface_default.xml')
mouth_cascade = cv2.CascadeClassifier('data\\xml\\haarcascade_mcs_mouth.xml')

count = 0

# Cahaya
bw_threshold = 80

# Pesan
font = cv2.FONT_HERSHEY_DUPLEX
org = (30, 30)
weared_mask_font_color = (255, 255, 255)
not_weared_mask_font_color = (0, 0, 255)
thickness = 2
font_scale = 1
weared_mask = "Terimakasih Sudah Memakai Masker"
not_weared_mask = "Tolong Kenakan Masker Anda"
title = "Pendeteksi Masker"

# mengambil video menggunakan webcam
cap = cv2.VideoCapture(0)

# mengambil video menggunakan video yg sudah ada 
# cap = cv2.VideoCapture('test.mp4')

while 1:
    # mengatur frame
    ret, img = cap.read()
    img = cv2.flip(img,1)

    # konversi gambar
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # konversi hitam putih
    (thresh, black_and_white) = cv2.threshold(gray, bw_threshold, 255, cv2.THRESH_BINARY)

    # pendeteksian wajah
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # pendeteksian wajah dengan skema hitam putih
    faces_bw = face_cascade.detectMultiScale(black_and_white, 1.1, 4)


    if(len(faces) == 0 and len(faces_bw) == 0):
        cv2.putText(img, "Wajah Tidak Terdeteksi...", org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
    elif(len(faces) == 0 and len(faces_bw) == 1):
        doorAutomate(0)
        # It has been observed that for white mask covering mouth, with gray image face prediction is not happening
        cv2.putText(img, weared_mask, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
    else:
        # tanda persegi di wajah
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            # pendeteksi mulut
            mouth_rects = mouth_cascade.detectMultiScale(gray, 1.5, 5)

        # Face detected but Lips not detected which means person is wearing mask
        if(len(mouth_rects) == 0):
            doorAutomate(0)
            cv2.putText(img, weared_mask, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
        else:
            for (mx, my, mw, mh) in mouth_rects:
                if(y < my < y + h):
                    cv2.putText(img, not_weared_mask, org, font, font_scale, not_weared_mask_font_color, thickness, cv2.LINE_AA)
                    cv2.rectangle(img, (mx, my), (mx + mh, my + mw), (0, 0, 255), 3)
                    winsound.PlaySound('sound/alert.wav', winsound.SND_FILENAME)
                    new_image = cv2.putText(
                                            img = img,
                                            text = "Gambar Disimpan",
                                            org = (200, 200),
                                            fontFace = cv2.FONT_HERSHEY_DUPLEX,
                                            fontScale = 1.0,
                                            color = (125, 246, 55),
                                            thickness = 3
                                            )
                    file = 'C:/test/data'+str(count)+'.jpg'
                    cv2.imwrite(file, img)
                    count +=1
                    break

    # fungsi menampilkan dan exit
    cv2.imshow(title, img)
    keyCode = cv2.waitKey(1)
    if cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) < 1:
        break

# exit
cap.release()
cv2.destroyAllWindows()
