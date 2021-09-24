import time
import random
import cv2
import dropbox

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    #initialising cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        #cv2.imwrite() this method is used to save an image to any storage device
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    print("snapshot taken")
    #releases the camera
    videoCaptureObject.release()
    #closes all the windows that might be opened during this process
    cv2.destroyAllWindows()
    return img_name

def upload_file(img_name):
    access_token="Hn1jE9iitoEAAAAAAAAAAcyrJpNDBYAINBkyNpTEyZ_LGNZvBQ8NfYBDcol69W15"
    file=img_name
    file_from=file
    file_to="/newFolder1"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')
def main():
    while(True):
        if ((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()
