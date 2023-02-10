from config import *

class road:
    def __init__(self):
        pass

    # Mapping road conditions
    def draw_road(self):
        glBegin(GL_QUADS)

        glColor4f(0.8, 0.8, 0.8, 1.0)
        glVertex3f(100.0, 100.0, 0.)
        glVertex3f(100.0, -100.0, 0.)
        glVertex3f(-100.0, -100.0, 0.)
        glVertex3f(-100.0, 100.0, 0.)

        glEnd()