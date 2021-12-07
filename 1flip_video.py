import cv2
nama = 'flipvideo'

capture = cv2.VideoCapture(0)
while True:
    ret, img = capture.read()
    img = cv2.flip(img,1) # berdasarkan nilai netral positif negetif
    cv2.imshow(nama, img)
    keyCode = cv2.waitKey(1)# jika 1 diganti 0 maka akan hanya muncul gambar 
    # untuk menahan gambar agar selalu loop
    if cv2.getWindowProperty(nama, cv2.WND_PROP_VISIBLE) < 1:
        break
