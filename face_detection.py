from cv2 import CascadeClassifier, imread, cvtColor, COLOR_BGR2GRAY, rectangle, resize
face_cascade = CascadeClassifier('C:\\Users\\mika\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

def read(file):
    return imread(file)

def face_detect(img):
    gray = cvtColor(img, COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.03, minNeighbors=3, minSize=(60, 60), maxSize=(130, 130))
    for (x,y,w,h) in faces:
        rectangle(gray,(x,y),(x+w,y+h),(255,0,0),1)
    return gray

def is_face(img):
    gray = cvtColor(img, COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors=5, minSize=(60, 60))
    return not (faces is ())

def is_face_gs(img):
    faces = face_cascade.detectMultiScale(img, scaleFactor = 1.05, minNeighbors=5, minSize=(60, 60))
    return not (faces is ())

def is_face_sz(img, min_s):
    faces = face_cascade.detectMultiScale(img, scaleFactor = 1.05, minNeighbors=5, minSize=(min_s, min_s))
    return not (faces is ())

def crop(img):
    gray = cvtColor(img, COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.03, minNeighbors=5, minSize=(60, 60), maxSize=(130, 130))
    res = ()
    if len(faces)>0:
        for (x,y,w,h) in faces:
            cropped_img = gray[y:y+h, x:x+w]
            if is_face_gs(cropped_img):
                res = cropped_img
    return res


if __name__ == "__main__":
    import sys
    imgray = face_detect(sys.argv[1])
    face = is_face(sys.argv[1])
    if face:
        print(sys.argv[1], imgray)
    else: print('No face has been detected')
