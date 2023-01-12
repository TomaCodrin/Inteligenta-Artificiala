import cv2
import keyboard
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
#Utilizam camera web ca si input
while not keyboard.is_pressed('esc'):
	_, img = cap.read()
	#convertim in alb negru
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#Detectam fetele (pot fi si negre :| )
	faces = face_cascade.detectMultiScale(gray,1.1,4)
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
	cv2.imshow('Img', img)

	k = cv2.waitKey(30) &  0xff
	if k==27:
		break

cap.release()
