import cv2
face_cascade = cv2.CascadeClassifier('C:\\Users\\mika\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

def read(file):
    return cv2.imread(file)

def face_detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    for (x,y,w,h) in faces:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),1)
    return gray

def is_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return not faces is ()

if __name__ == "__main__":
    import sys
    imgray = face_detect(sys.argv[1])
    face = is_face(sys.argv[1])
    if face:
        print(sys.argv[1], imgray)
    else: print('No face has been detected')
