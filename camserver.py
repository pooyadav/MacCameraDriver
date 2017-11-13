#!/usr/bin/bash
# -*- coding: utf-8 -*- 

import cv2
import os
import base64
import numpy as np
from flask import Flask,  Response



app = Flask(__name__)
cap = cv2.VideoCapture(0)

@app.route('/')
def index():
    return("CamServer running now!")

@app.route('/video_feed')
def video_feed():

    print("inside index")
    success, frame = cap.read()
    #print(frame)
    ret, jpeg = cv2.imencode('.jpg', frame)
    byteframe = jpeg.tobytes()
    return Response(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + byteframe + b'\r\n\r\n',
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
