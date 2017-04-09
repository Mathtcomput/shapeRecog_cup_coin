import cv2
vc = cv2.VideoCapture('cup_1.MOV')
fps = vc.get(cv2.cv.CV_CAP_PROP_FPS)
cup_cascade = cv2.CascadeClassifier('cascade.xml')
videoWriter = cv2.VideoWriter('Myout.avi',cv2.cv.CV_FOURCC('M','J','P','G'),fps,(1280,720))
success ,frame = vc.read()
while success:
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cups = cup_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,h,w) in cups:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    videoWriter.write(frame)
    success ,frame = vc.read()



'''        
    cv2.namedWindow('cups Detected!')
    cv2.imshow('cups Detected!',img)
    cv2.imwrite('cups.jpg',img)
    cv2.waitKey(0)
'''
