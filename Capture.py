import numpy as np
import cv2


class Capture:
    w: int
    h: int
    fourcc: cv2.VideoWriter_fourcc
    out: cv2.VideoWriter()

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        fps = 60.0
        self.out = cv2.VideoWriter('output.avi', self.fourcc, fps, (self.w, self.h))

    def record(self, data: np.ndarray):
        self.out.write(data)

    def create_movie(self):
        self.out.release()
