import numpy as np
from random import random

from Particle import Particle
from typing import List


def rand():
    return (2.0 * random()) - 1.0


def simulation_step(p_vector: List[Particle], dt: float):
    damp = 0.98  # damping factor for original velocity
    f = 0.005  # factor for velocity change in each step

    for particle in p_vector:
        particle.m_position += dt * particle.m_velocity
        particle.m_velocity = damp * particle.m_velocity + np.array([rand(), rand()]) * f
