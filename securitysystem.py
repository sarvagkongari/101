import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(True):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token="sl.BFw5N6dlk9HHgzrOJYOn7LadBK7HeI-OP9whRL_6jsvokkDFEXrjvmVqs6QrkI-0Q8NwFGrkOwuQU39KETIuz5TFYIjXLKpV7HYq9RqDWPXg__2x_o1BhqhV6kRl61DCoVkjE540FWKr"
    file=img_name
    file_from=file 
    file_to="/NewFolder1/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)

main()