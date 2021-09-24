import cv2

def take_snapshot():
    # initialising cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        #cv2.imwrite() this method is used to save an image to any storage device
        cv2.imwrite("NewPicture1.jpg",frame)
        result=False
    #releases the camera
    videoCaptureObject.release()
    #closes all the windows that might be opened during this process
    cv2.destroyAllWindows()
take_snapshot()   

