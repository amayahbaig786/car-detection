import cv2

video = cv2.VideoCapture('video.avi')

car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    ret,frames = video.read()
    gray = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,1)
    #draw rectangles around the cars
    for(x,y,w,h)in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(245,230,3),2)
    
    cv2.imshow("video2",frames)

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
