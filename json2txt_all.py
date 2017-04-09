import json
def loadFont():
    for j in range(6)[1:]:
        f = open("cup_%d.json"%j)  
        jsondata = json.load(f)
        r = open("train.txt","a+")
        flist = jsondata['video_annotations']
        for i in range(len(flist)):
            tmp = flist[i]['frame_annotations'][0]
            r.write("image_%d_"%j+str(flist[i]['frame'])+".jpg"+"\t"+"1"+"\t"+str(tmp['min_x'])+"\t"+str(tmp['min_y'])+
                    "\t"+str(tmp['max_x']-tmp['min_x'])+"\t"+str(tmp['max_y']-tmp['min_y'])+"\n")
        f.close()
    r.close()

if __name__ == "__main__":
    loadFont()
    

