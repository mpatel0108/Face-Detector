import cv2
from random import randrange

#Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect faces in
#img = cv2.imread('All.jpg')

#To capture video from Video
#webcam = cv2.VideoCapture("Video.MP4")
#To capture video from webcam
webcam = cv2.VideoCapture(0)

#Iterate forever over frames
while True:

    #Read the current frames
    succeccful_frame_read, frame = webcam.read()

    #Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #Draw rectangle around the faces
    for (x, y, w, h) in face_coordinates:
        #(x, y, w, h) = face_coordinates[0]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256),randrange(256),randrange(256)), 10)

    cv2.imshow('Man Patel Face Detector', frame)
    key= cv2.waitKey(1)

    #Stop if Q key is pressed
    if key==81 or key==113:
        break

#Release the VideoCapture object
webcam.Release()

print("Code Completed")

'''
#Must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect Faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#Draw rectangle around the faces
for (x, y, w, h) in face_coordinates:
#(x, y, w, h) = face_coordinates[0]
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256),randrange(256),randrange(256)), 4)


#Display the image with faces
cv2.imshow('Man Patel Face Detector', img)
cv2.waitKey()
'''
