from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np
import sys
from typing import List

from Particle import Particle
import Solver
from CircularWireConstraint import CircularWireConstraint
from SpringForce import SpringForce
from Capture import Capture

# Global variables
N = 0
dt, d = 0.0, 0.0
d_sim = False  # int in skeleton, used as bool
dump_frames = 0.0
frame_number = 0.0
p_vector: List[Particle] = []  # vector containing particles
win_id = 0
win_x, win_y = 0, 0
mouse_down = [0, 0, 0]
mouse_release = [0, 0, 0]
mouse_shiftclick = [0, 0, 0]
omx, omy, mx, my = 0, 0, 0, 0
hmx, hmy = 0, 0
capture: Capture = None  # class to catch screenshots and create movie

#static RodConstraint # delete_this_dummy_rod = NULL
delete_this_dummy_spring: SpringForce = None  # delete_this_dummy_spring = NULL
delete_this_dummy_wire: CircularWireConstraint = None  # delete_this_dummy_wire = NULL


def free_data():
    global delete_this_dummy_spring, delete_this_dummy_wire
    delete_this_dummy_spring = None
    delete_this_dummy_wire = None


def init_system():
    dist = 0.2
    center = np.array([0.0, 0.0])
    offset = np.array([dist, 0.0])
    
    # Create three particles, attach them to each other, then add a
    # circular wire constraint to the first.

    global p_vector, delete_this_dummy_spring, delete_this_dummy_wire
    p_vector.append(Particle(center + offset))
    p_vector.append(Particle(center + offset + offset))
    p_vector.append(Particle(center + offset + offset + offset))
    
    # You should replace these with a vector generalized forces and one of constraints
    delete_this_dummy_spring = SpringForce(p_vector[0], p_vector[1], dist, 1.0, 1.0)
    # delete_this_dummy_rod = new RodConstraint(pVector[1], pVector[2], dist)
    delete_this_dummy_wire = CircularWireConstraint(p_vector[0], center, dist)


def pre_display():
    glViewport(0, 0, win_x, win_y)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)


def post_display():
    global frame_number
    # Write frames if necessary
    if dump_frames:
        frame_interval = 4

        if (frame_number % frame_interval) == 0:
            w = glutGet(GLUT_WINDOW_WIDTH)
            h = glutGet(GLUT_WINDOW_HEIGHT)
            global capture
            if capture is None:
                capture = Capture(w, h)

            glPixelStorei(GL_PACK_ALIGNMENT, 1)
            capture.record(glReadPixels(0, 0, w, h, GL_RGBA, GL_BYTE))
    else:
        if capture is not None:
            capture.create_movie()
            capture = None

    glutSwapBuffers()


def draw_particles():
    for par in p_vector:
        par.draw()


def draw_forces():
    # change this to iteration over full set
    delete_this_dummy_spring.draw()


def draw_constraints():
    # change this to iteration over full set
    delete_this_dummy_wire.draw()


def clear_data():
    for par in p_vector:
        par.reset()


def mouse_func(button, state, x, y):
    global omx, mx, my, hmx, hmy
    omx = mx = x
    omx = my = y

    if not mouse_down[0]:
        hmx = x
        hmy = y
    if mouse_down[button]:
        mouse_release[button] = state == GLUT_UP
        mouse_shiftclick[button] = glutGetModifiers() == GLUT_ACTIVE_SHIFT
    mouse_down[button] = state == GLUT_DOWN

    
def motion_func(x: int, y: int):
    global mx, my
    mx = x
    my = y


def display_func():
    pre_display()

    draw_forces()
    draw_constraints()
    draw_particles()

    post_display()


def idle_func():
    global d_sim, win_id, p_vector, dt
    if d_sim:
        Solver.simulation_step(p_vector, dt)
    else:
        # get_from_UI() needs to be implemented
        remap_gui()

    glutSetWindow(win_id)
    glutPostRedisplay()


def remap_gui():
    for par in p_vector:
        par.m_position[0] = par.m_construct_pos[0]
        par.m_position[1] = par.m_construct_pos[1]


def key_func(key, x, y):
    key = key.decode("utf-8")
    if key == 'c' or key == 'C':
        clear_data()
    elif key == 'd' or key == 'D':
        global dump_frames
        dump_frames = not dump_frames
    elif key == 'q' or key == 'Q':
        free_data()
        sys.exit(0)
    elif key == ' ':
        global d_sim
        d_sim = not d_sim
        

def open_glut_window():
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)

    glutInitWindowPosition(0, 0)
    glutInitWindowSize(win_x, win_y)
    global win_id
    win_id = glutCreateWindow(b"Particletoys!")

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glutSwapBuffers()
    glClear(GL_COLOR_BUFFER_BIT)
    glutSwapBuffers()

    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_POLYGON_SMOOTH)

    pre_display()

    glutKeyboardFunc(key_func)
    glutMouseFunc(mouse_func)
    glutMotionFunc(motion_func)
    #glutReshapeFunc(reshape_func)
    glutIdleFunc(idle_func)
    glutDisplayFunc(display_func)


def main():
    glutInit(sys.argv)

# if(argc == 1):
    global N, dt, d
    N = 64
    dt = 0.5  # displacement of particles in each step
    d = 5.0
    print("Error: Using defaults : N=%d dt=%g d=%g\n", N, dt, d)
# else:
#    N = int(argv[1])
#    dt = float(argv[2])
#    d = float(argv[3])

    print("\n\nHow to use this application:\n\n")
    print("\t Toggle ruction/simulation display with the spacebar key\n")
    print("\t Dump frames by pressing the 'd' key\n")
    print("\t Quit by pressing the 'q' key\n")

    global d_sim, dump_frames, frame_number, win_x, win_y
    d_sim = False
    dump_frames = 0
    frame_number = 0

    init_system()

    win_x = 512
    win_y = 512
    open_glut_window()

    glutMainLoop()


if __name__ == '__main__': 
    main()
