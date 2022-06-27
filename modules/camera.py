from modules.stream import Stream


class VideoCamera:
    def __init__(self):
        self.video = Stream()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()

        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV

        ret, jpeg = self.video.imencode(typ='.jpg', frame=frame)

        return jpeg.tobytes()

    def gen(self):
        while True:
            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + self.get_frame() + b'\r\n\r\n'
