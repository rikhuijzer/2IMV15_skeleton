from OpenGL.GL import *
import numpy as np
from math import pi, cos, sin

from Particle import Particle


class CircularWireConstraint:
    m_p: Particle
    m_center: np.array
    m_radius: float  # originally double

    def __init__(self, par: Particle, center: np.array, dist: float):
        self.m_p = par
        self.m_center = center
        self.m_radius = dist

    @staticmethod
    def draw_circle(vect: np.array, radius: float):
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 1.0, 0.0)

        for i in range(0, 360, 18):
            deg_in_rad = i * pi / 180
            glVertex2f(vect[0] + cos(deg_in_rad) * radius, vect[1] + sin(deg_in_rad) * radius)

        glEnd()

    def draw(self):
        CircularWireConstraint.draw_circle(self.m_center, self.m_radius)