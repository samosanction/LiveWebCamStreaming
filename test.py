video = cv2.VideoCapture(0)


def get_frame():
    while True:
        success, frame = video.read()
        sc, encoded_image = cv2.imencode('.jpg', frame)
        frame = encoded_image.tobytes()
        yield (b'--frame\r\n Content-Type:image/jpeg\r\n\r\n' + frame + b'\r\n')


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vide_feed_url')
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# THIS to view output on this system

#if __name__ == "__main__":
    #app.run(debug=True)

    # OR

# to access the streaming on another device on the same network
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
# Then connect to same wifi and input IP_OF_MY_DEVICE/5001
