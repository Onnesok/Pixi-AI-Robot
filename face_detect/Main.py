import threading
import os
import pickle
import cv2
import face_recognition
import cvzone
import numpy as np
import csv
from datetime import datetime
import time
import pyttsx3


cap = cv2.VideoCapture(1)
# cap.set(3, 640)
# cap.set(4, 480)

# Load the encoding file
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, detectID = encodeListKnownWithIds
print(detectID)
print("Encode File Loaded")

id = -1
imgStudent = []
studentInfo = []



pixi = pyttsx3.init()
rate = pixi.getProperty('rate')
pixi.setProperty('rate', rate - 30)
voices = pixi.getProperty('voices')
pixi.setProperty('voice', voices[0].id)

# Talk a string
def talk(x):
    pixi.say(x)
    pixi.runAndWait() 

def read(id):
    print(id)
    try:
        id = str(id)
        with open(f'./info/eub/{id}.txt', 'r',encoding="utf8") as file:
            text = file.read()
            talk(text) 
            file.close()  
    except Exception as e:
        print(e)




def adjust_brightness(value):
    global brightness
    brightness = value / 100
    #print(f"Brightness set to {brightness}")

def adjust_contrast(value):
    global contrast
    contrast = value / 100
    #print(f"Contrast set to {contrast}")

def main():
    global id, imgBackground, studentInfo, imgStudent,brightness, contrast
    brightness = 1.0
    contrast = 1.0

    cv2.namedWindow("Face Recognition")
    cv2.createTrackbar("Brightness", "Face Recognition", 100, 200, adjust_brightness)
    cv2.createTrackbar("Contrast", "Face Recognition", 100, 200, adjust_contrast)

    recognized_faces = set()
    info_threads = {}
    fetching_thread = None
    showing_thread = None

    while True:
        success, img = cap.read()

        # Adjust brightness and contrast
        img = cv2.convertScaleAbs(img, alpha=brightness, beta=(1.0 - contrast) * 255)

        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faceCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

        if faceCurFrame:
            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance=0.5)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    bbox = x1, y1, x2 - x1, y2 - y1
                    img = cvzone.cornerRect(img, bbox, rt=0)

                    id = detectID[matchIndex]
                    print(id)

                    if id not in recognized_faces:
                        recognized_faces.add(id)

                        if id not in info_threads:
                            info_threads[id] = threading.Thread(target=lambda : read(id))
                            info_threads[id].start()
                            break

                        if info_threads[id] is not None and not info_threads[id].is_alive():
                            info_threads[id].join()
                            info_threads[id] = None

        # cv2.imshow("Face Attendance", img)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('r'):
            recognized_faces.clear()
            for thread in info_threads.values():
                if thread is not None and thread.is_alive():
                    thread.join()
            info_threads.clear()

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
