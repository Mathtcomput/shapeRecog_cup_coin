import cv2
f = open("train.txt")
datalist = []
for line in f.readlines():
    datalist.append(line.strip().split('\t')[0])
vc = cv2.VideoCapture('cup_1.MOV')
c=1
if vc.isOpened(): 
    rval , frame = vc.read()
else:
    rval = False 
while rval:   
    rval, frame = vc.read()
    if str(c) in datalist: 
        cv2.imwrite('image_1_'+str(c) + '.jpg',frame)
    c = c + 1
    cv2.waitKey(1)
vc.release()
print datalist
