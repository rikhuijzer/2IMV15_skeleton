from OpenGL.GL import *
from Particle import Particle


class SpringForce:
    m_p1: Particle  # particle 1
    m_p2: Particle  # particle 2
    m_dist: float  # rest length
    m_ks: float  # spring strength constants
    m_kd: float  # spring strength constants

    def __init__(self, p1: Particle, p2: Particle, dist: float, ks: float, kd: float):
        self.m_p1 = p1
        self.m_p2 = p2
        self.m_dist = dist
        self.m_ks = ks
        self.m_kd = kd

    def draw(self):
        glBegin(GL_LINES)
        glColor3f(0.6, 0.7, 0.8)
        glVertex2f(self.m_p1.m_position[0], self.m_p1.m_position[1])
        glColor3f(0.6, 0.7, 0.8)
        glVertex2f(self.m_p2.m_position[0], self.m_p2.m_position[1])
        glEnd()
