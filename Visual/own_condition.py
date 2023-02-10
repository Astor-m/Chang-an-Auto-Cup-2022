from config import *


class own:

    def __init__(self, color, head_angle):
        self.head_angle = head_angle
        self.color = color

    # Mapping its own car body
    def draw_own(self):
        p = [0.0, 0.0, 0.1]

        glBegin(GL_QUADS)

        # Front end
        glColor4f(0.95, 0.95, 0.95, 0.0)
        glVertex3f(p[0] + 1, p[1] + 3, p[2])
        glVertex3f(p[0] - 1, p[1] + 3, p[2])
        glVertex3f(p[0] - 0.9, p[1] + 2.6, p[2] + 1)
        glVertex3f(p[0] + 0.9, p[1] + 2.6, p[2] + 1)

        # Engine cover
        glColor4f(0.9, 0.9, 0.9, 0.0)
        glVertex3f(p[0] + 0.9, p[1] + 2.6, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + 2.6, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + 1.2, p[2] + 1)
        glVertex3f(p[0] + 0.9, p[1] + 1.2, p[2] + 1)

        # 挡风玻璃
        glColor4f(0.98, 0.98, 0.98, 1)
        glVertex3f(p[0] + 0.9, p[1] + 1.2, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + 1.2, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + 0.8, p[2] + 1.5)
        glVertex3f(p[0] + 0.9, p[1] + 0.8, p[2] + 1.5)

        # Car roof
        glColor4f(0.9, 0.9, 0.9, 0.0)
        glVertex3f(p[0] + 0.9, p[1] + 0.8, p[2] + 1.5)
        glVertex3f(p[0] - 0.9, p[1] + 0.8, p[2] + 1.5)
        glVertex3f(p[0] - 0.9, p[1] + -0.8, p[2] + 1.5)
        glVertex3f(p[0] + 0.9, p[1] + -0.8, p[2] + 1.5)

        glColor4f(0.98, 0.98, 0.98, 1)
        glVertex3f(p[0] + 0.9, p[1] + -0.8, p[2] + 1.5)
        glVertex3f(p[0] - 0.9, p[1] + -0.8, p[2] + 1.5)
        glVertex3f(p[0] - 0.9, p[1] + -1.2, p[2] + 1)
        glVertex3f(p[0] + 0.9, p[1] + -1.2, p[2] + 1)

        glColor4f(0.9, 0.9, 0.9, 0.0)
        glVertex3f(p[0] + 0.9, p[1] + -1.2, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + -1.2, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + -2.2, p[2] + 1)
        glVertex3f(p[0] + 0.9, p[1] + -2.2, p[2] + 1)

        glColor4f(0.9, 0.9, 0.9, 0.0)
        glVertex3f(p[0] + 0.9, p[1] + -2.2, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + -2.2, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + -2.5, p[2])
        glVertex3f(p[0] + 0.9, p[1] + -2.5, p[2])

        glColor4f(0.9, 0.9, 0.9, 0.0)
        glVertex3f(p[0] + 0.9, p[1] + 3.0, p[2])
        glVertex3f(p[0] - 0.9, p[1] + 3.0, p[2])
        glVertex3f(p[0] - 0.9, p[1] + -2.5, p[2])
        glVertex3f(p[0] + 0.9, p[1] + -2.5, p[2])

        glEnd()

        # left
        glBegin(GL_POLYGON)
        glColor4f(0.9, 0.9, 0.9, 0.0)
        glVertex3f(p[0] + 0.9, p[1] + 3.0, p[2])
        glVertex3f(p[0] + 0.9, p[1] + 2.6, p[2] + 1)
        glVertex3f(p[0] + 0.9, p[1] + 1.2, p[2] + 1)
        glVertex3f(p[0] + 0.9, p[1] + 0.8, p[2] + 1.5)
        glVertex3f(p[0] + 0.9, p[1] + -0.8, p[2] + 1.5)
        glVertex3f(p[0] + 0.9, p[1] + -1.2, p[2] + 1)
        glVertex3f(p[0] + 0.9, p[1] + -2.2, p[2] + 1)
        glVertex3f(p[0] + 0.9, p[1] + -2.5, p[2])
        glEnd()

        # right
        glBegin(GL_POLYGON)
        glVertex3f(p[0] - 0.9, p[1] + 3.0, p[2])
        glVertex3f(p[0] - 0.9, p[1] + 2.6, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + 1.2, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + 0.8, p[2] + 1.5)
        glVertex3f(p[0] - 0.9, p[1] + -0.8, p[2] + 1.5)
        glVertex3f(p[0] - 0.9, p[1] + -1.2, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + -2.2, p[2] + 1)
        glVertex3f(p[0] - 0.9, p[1] + -2.5, p[2])
        glEnd()

        # Tires
        glBegin(GL_LINES)
        glColor4f(0.0, 0.0, 0.0, 0.0)
        for i in range(64):
            glVertex3f(p[0] - 0.9, p[1] + -1.8, p[2] + 0.45)
            glVertex3f(-0.9, 0.35 * math.sin(2 * math.pi * i / 64) + 0.45, 0.35 * math.cos(2 * math.pi * i / 64))

        for i in range(64):
            glVertex3f(p[0] - 0.9, p[1] + 1.8, p[2] + 0.45)
            glVertex3f(-0.9, 0.35 * math.sin(2 * math.pi * i / 64) + 0.45, 0.35 * math.cos(2 * math.pi * i / 64))
        glEnd()