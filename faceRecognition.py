import cv2

face_cascade_path = '/usr/local/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml'
eye_cascade_path = '/usr/local/lib/python3.9/site-packages/cv2/data/haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# 絶対pathではないと読み込まないはず。
IMAGE_PATH = "~/Desktop/IMG_0065.jpeg"


src = cv2.imread(IMAGE_PATH)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray)

for x, y, w, h in faces:
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 5)
    face = src[y: y + h, x: x + w]
    face_gray = src_gray[y: y + h, x: x + w]
    eyes = eye_cascade.detectMultiScale(face_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

cv2.imwrite("~/Desktop/sample.jpeg", src)
