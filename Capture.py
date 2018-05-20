import numpy as np
import cv2


class Capture:
    out: cv2.VideoWriter()

    def __init__(self, w, h):
        four_cc = cv2.VideoWriter_fourcc(*'MJPG')
        fps = 60.0
        self.out = cv2.VideoWriter('output.avi', four_cc, fps, (w, h))

    def record(self, data: np.ndarray):
        self.out.write(data)

    def create_movie(self):
        self.out.release()
