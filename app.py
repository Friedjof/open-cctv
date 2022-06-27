import secrets

from flask import Flask, render_template, Response, request, session, redirect

from modules.camera import VideoCamera
from modules.model.models import *

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)

video_stream = VideoCamera()


@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(f'/user/{session["user"]}')


@app.route('/login', methods=['POST'])
def login():
    user: User = User.get_or_none(User.username == f"{request.form['username']}")
    if user is not None:
        if user.password == request.form['password']:
            session['logged_in'] = True
            session['user'] = request.form['username']
    return redirect(f'/user/{session["user"]}')


@app.route("/user/<name>")
def home(name):
    if "user" in tuple(session.keys()):
        if name == session["user"]:
            return render_template('index.html', username=name)
        else:
            return redirect(f'/user/{session["user"]}')
    else:
        return redirect('/')


@app.route('/video_feed')
def video_feed():
    return Response(video_stream.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.errorhandler(404)
def not_found(_):
    return redirect('/')


if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)
