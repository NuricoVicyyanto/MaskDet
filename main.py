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
weared_mask = "Terimakasih Sudah Memakai Masker"
not_weared_mask = "Tolong Kenakan Masker Anda"
title = "Pendeteksi Masker"

# mengambil video menggunakan webcam
capture =   cv2.VideoCapture(0)

while True:
    # mengatur frame
    ret, img = capture.read()#membaca gambar yang diperoleh dari video
    """
    - ret adalah variabel boolean yang kembali benar jika frame tersedia.
    - img adalah vektor array gambar yang diambil berdasarkan img default 
        per detik yang didefinisikan secara eksplisit atau implisit
    """

    img = cv2.flip(img,1)
    # array; 0 berarti membalik-balik sumbu x dan 
    # nilai positif (misalnya, 1) berarti membalik-balik sumbu y. 
    # Nilai negatif (misalnya, -1) berarti membalik-balik kedua sumbu.

    # konversi gambar
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cvtColor pada opencv berfungsi untuk mengkonversi warna menjadi abu-abu dan img adalah
    # gambar yang akan dirubah warnanya

    # konversi hitam putih
    (thresh, black_and_white) = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    # cv2.threshold adalah fungsi untuk Thresholding, Binarization adalah proses mengubah 
    # sebuah image kedalam bentuk binary, Untuk melakukan thresholding, image harus diconvert menjadi image grayscale.
    # cv2.threshold(gambar gray yg akan dideteksi, nilai treeshold, max nilai threeshold, tipe threshold)

    # pendeteksian wajah
    wajah = face_cascade.detectMultiScale(gray, 1.1, 3)
    # detect multiscale inputnya berupa gambar yang telah diubah menjadi binary beserta scale factor dan minimal
    # tetangga pixel terdekat yg hampir mirip
    # cv.CascadeClassifier.detectMultiScale2(	image[, scaleFactor[, minNeighbors]]]]


    # pendeteksian wajah dengan skema hitam putih
    wajah_hitam_putih = face_cascade.detectMultiScale(black_and_white, 1.1, 3)
    # detect multiscale inputnya berupa gambar yang telah diubah menjadi binary beserta scale factor dan minimal
    # tetangga pixel terdekat yg hampir mirip
    # cv.CascadeClassifier.detectMultiScale2(	image[, scaleFactor[, minNeighbors]]]]

    """
    parameter detect multiscale
    - citra	Matriks tipe CV_8U yang berisi gambar di mana objek terdeteksi.
    - objek	Vektor persegi panjang di mana setiap persegi panjang berisi objek yang terdeteksi, persegi panjang mungkin sebagian di luar gambar asli.
    - scaleFactor	Parameter yang menentukan berapa banyak ukuran gambar dikurangi pada setiap skala gambar.
    - minNeighbors	Parameter yang menentukan berapa banyak tetangga setiap kandidat persegi panjang harus mempertahankannya.
    - flags	Parameter dengan arti yang sama untuk kaskade lama seperti dalam fungsi cvHaarDetectObjects. Ini tidak digunakan untuk kaskade baru.
    - minSize	Ukuran objek minimum yang mungkin. Objek yang lebih kecil dari itu diabaikan.
    - maxSize	Ukuran objek maksimum yang mungkin. Objek yang lebih besar dari itu diabaikan. Jika model dievaluasi dalam skala tunggal.maxSize == minSize
    """


    if(len(wajah) == False and len(wajah_hitam_putih) == False):
        cv2.putText(img, ".", org, font, ukuran_font, warna_font_pakai_masker, ketebalan, cv2.LINE_AA)
    elif(len(wajah) == False and len(wajah_hitam_putih) == True):
        #doorAutomate(0)
        # It has been observed that for white mask covering mouth, with gray image face prediction is not happening
        cv2.putText(img, weared_mask, org, font, ukuran_font, warna_font_pakai_masker, ketebalan, cv2.LINE_AA)
    else:
        # tanda persegi di wajah
        for (x, y, w, h) in wajah:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            # pendeteksi mulut
            mulut = mouth_cascade.detectMultiScale(gray, 1.1, 3)

        # kondisi ketika mulut tidak terdeteksi maka diasumsikan orang 
        # tersebut memakai beserta masker
        if(len(mulut) == False):
            # doorAutomate(0)
            cv2.putText(img, weared_mask, org, font, ukuran_font, warna_font_pakai_masker, ketebalan, cv2.LINE_AA)
        else:
            for (mx, my, mw, mh) in mulut:
                if(y < my < y + h):
                    cv2.putText(img, not_weared_mask, org, font, ukuran_font, warna_font_tidak_pakai_masker, ketebalan, cv2.LINE_AA)
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
capture.release()
cv2.destroyAllWindows()