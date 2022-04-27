import csv

import cv2
import csv
from cvzone.HandTrackingModule import HandDetector
import cvzone

class MCQ():
    def __init__(self, data):
        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.answer = int(data[5])

        self.userAns = None



cap = cv2.VideoCapture(0)
cap.set(3, 1288)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
pathCSV = "Mcqs.csv"
with open(pathCSV) as f:
    reader = csv.reader(f)
    dataAll = list(reader)[1:]

mcqList = []
for q in dataAll:
    mcqList.append(MCQ(q))
print(len(mcqList))

qNo = 0
qTotal = len(dataAll)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    mcq = mcqList[0]

    cvzone.putTextRect(img, )

    cv2.imshow("Img", img)
    cv2.waitKey(1)
