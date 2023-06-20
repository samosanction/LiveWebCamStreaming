import cv2
from flask import Flask, render_template, Response

video = cv2.VideoCapture(1)

def get_frame():
    success, frame = video.read()
    sc, encode_image = cv2.imencode('.jpg', frame)
    frame = encoded_image.tobytes()
    yield b'--frame\r\n Content-Type:image/jpeg\r\n\r\n' + frame + b'\r\n'

app = Flask(__name__)
