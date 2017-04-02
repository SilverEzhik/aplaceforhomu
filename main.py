#!/usr/bin/env python3

#https://github.com/log0/video_streaming_with_flask_example

from flask import Flask, render_template, Response
from place import bitmap_to_jpg
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        sleep(5)
        frame = bitmap_to_jpg()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
