from flask import render_template, request
from flask import redirect, url_for
import os
from PIL import Image
from app.utils import pipeline_model
from app.utils import pipeline_model1
import cv2


UPLOAD_FLODER = 'static/uploads'
def base():
    return render_template('base.html')


def index():
    return render_template('index.html')


def faceapp():
    return render_template('faceapp.html')

def getwidth(path):
    img = Image.open(path)
    size = img.size # width and height
    aspect = size[0]/size[1] # width / height
    w = 300 * aspect
    return int(w)

def video(n=1):
    
    if n==0:
        print("dsds")
        cap = cv2.VideoCapture(0)
        while(True): 
      
            # Capture the video frame 
            # by frame 
            ret, frame = cap.read() 
            frame = pipeline_model1(frame,color='bgr')
            # Display the resulting frame 
            cv2.imshow('frame', frame) 
            
            # the 'q' button is set as the 
            # quitting button you may use any 
            # desired button of your choice 
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
    if request.method == "POST":
        f = request.files['video']
        filename=  f.filename
        path = os.path.join(UPLOAD_FLODER,filename)
        f.save(path)
        if n==1:
            cap = cv2.VideoCapture(path)
        else:
            cap = cv2.VideoCapture(0)
        #w = getwidth(path)
        # prediction (pass to pipeline model)
        while True:
            ret, frame = cap.read() # bgr

            if ret == False:
                break

            frame = pipeline_model1(frame,color='bgr')

            cv2.imshow('Gender Detector',frame)
            
            if cv2.waitKey(10) == ord('s'): # press s to exit  --#esc key (27), 
                break
        cv2.destroyAllWindows()
        cap.release()
        return render_template('gendervideo.html',fileupload=True,video_name=filename)


    return render_template('gendervideo.html',fileupload=False,video_name="freeai.png")
    
def gender():
    if request.method == "POST":
        f = request.files['image']
        filename=  f.filename
        path = os.path.join(UPLOAD_FLODER,filename)
        f.save(path)
        w = getwidth(path)
        # prediction (pass to pipeline model)
        pipeline_model(path,filename,color='bgr')
        return render_template('gender.html',fileupload=True,img_name=filename, w=w)

    return render_template('gender.html',fileupload=False,img_name="freeai.png")
