import os
import cv2

def detect_face(frame):
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_detect = face.detectMultiScale(color, 1.3, 5)
    for (x,y, w,h) in face_detect:
        cv2.rectangle(
            frame, (x,y),
            (x + w,y + h),
            (0, 255, 0),
            3,
        )
def detect_eye(frame):
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eye = cv2.CascadeClassifier('haarcascade_eye.xml')
    eye_detect = eye.detectMultiScale(color, 1.3, 5)
    for (x,y, w,h) in eye_detect:
        cv2.rectangle(
            frame, (x,y),
            (x + w,y + h),
            (0, 255, 0),
            3,
        )
def main():
    cam = cv2.VideoCapture(0)
    cam.set(3, 1920)
    cam.set(4, 1080)

    print("\n9's Detection Program")
    print("\nChoose detection mode: ")
    print("1. Face detection")
    print("2. Eye detection")
    pickanumber = input("Enter number: ")
        
    while True:
        _, frame = cam.read()
        if pickanumber == "1":
            detect_face(frame)
        elif pickanumber == "2":
            detect_eye(frame)
        else:
            print("No such menu.")
            break

        cv2.imshow("9's Detection Program",frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    
    cam.release()
    cv2.destroyAllWindows()

main()