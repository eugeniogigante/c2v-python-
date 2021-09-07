import cv2
import webcamModule


class FindFace() :
    def __init__(self):
        pass

    def findFace(self, img):
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 1.1, 6)

        myFaceListC = []
        myFaceListArea = []

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cx = x + w // 2
            cy = y + h // 2
            area = w * h
            myFaceListArea.append(area)
            myFaceListC.append([cx, cy])

        if len(myFaceListArea) != 0:
            i = myFaceListArea.index(max(myFaceListArea))
            return img, [myFaceListC[i], myFaceListArea[i]]
        else:
            return img, [[0, 0], 0]


def main():
    myFace = FindFace()
    img = webcamModule.getImg(True)
    myFace.findFace(img)



if __name__ == '__main__':

    main()
