import cv2

face_cascade_path = '/usr/local/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)

# 定数定義
ESC_KEY = 27
INTERVAL = 33

# カメラ映像取得
cap = cv2.VideoCapture(2)

# 初期フレームの読込
end_flag, c_frame = cap.read()

# 変換処理ループ
while end_flag == True:
    # 画像の取得と顔の検出
    src = c_frame
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(src_gray)

    for x, y, w, h in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 10)

    # フレーム表示
    cv2.imshow("src", src)

    # ESCキーで終了
    key = cv2.waitKey(INTERVAL)
    if key == ESC_KEY:
        break

    # 次のフレーム読込
    end_flag, c_frame = cap.read()

# 処理終了
cv2.destroyAllWindows()
cap.release()
