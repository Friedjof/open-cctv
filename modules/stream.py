import cv2


class Stream:
    def __init__(self, code: int = 0):
        self._stream: cv2.VideoCapture = cv2.VideoCapture(code)
        self.string: str = "string"

    def release(self):
        self._stream.release()

    def read(self) -> tuple:
        return self._stream.read()

    def imencode(self, frame, typ: str = '.jpg') -> tuple:
        return cv2.imencode(typ, frame)
