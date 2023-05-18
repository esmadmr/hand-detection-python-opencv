import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2,detectionCon=0.75)

while True:
    sucees,img = cap.read()
    img = cv2.flip(img,1)

    hands,img = detector.findHands(img)

    if hands:
        hand = hands[0]
        finger = detector.fingersUp(hand)
        print(finger)

    # Görüntüyü göster
    cv2.imshow('Hands Detect', img)

    # Klavyeden bir tuşa basılmasını bekleyin
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break