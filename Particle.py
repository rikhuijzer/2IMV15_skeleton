from OpenGL.GL import *
import numpy as np


class Particle:
    m_construct_pos = np.array([0.0, 0.0])
    m_position = np.array([0.0, 0.0])
    m_velocity = np.array([0.0, 0.0])

    def __init__(self, construct_pos):
        self.m_construct_pos = construct_pos

    # Particle::~Particle(void) {} virtual function appearing in C++ skeleton not implemented (yet)

        # added to avoid all Particles starting at (0.0, 0.0)
        self.m_position = construct_pos

    def reset(self):
        self.m_position = self.m_construct_pos
        self.m_velocity = [0.0, 0.0]

    def draw(self):
        h = 0.03
        glColor3f(1.0, 0.0, 0.0) 
        glBegin(GL_QUADS)
        glVertex2f(self.m_position[0] - h / 2.0, self.m_position[1] - h / 2.0)
        glVertex2f(self.m_position[0] + h / 2.0, self.m_position[1] - h / 2.0)
        glVertex2f(self.m_position[0] + h / 2.0, self.m_position[1] + h / 2.0)
        glVertex2f(self.m_position[0] - h / 2.0, self.m_position[1] + h / 2.0)
        glEnd()