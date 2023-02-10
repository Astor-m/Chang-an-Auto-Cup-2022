import numpy as np

from config import *


class obj:
    def __init__(self):
        pass

    # Obtain target information
    def get_obj_info(self, sstr, obj_parameter):
        sub_s = sstr
        objs = []
        sstart = 0
        for i in range(31):
            obj = []
            state = 0  # Are the goals valid
            sub_s = sub_s[sub_s.find('objs_') + 1:]

            for op in obj_parameter:
                if op == obj_parameter[0]:
                    if sub_s[sub_s.find(op) + len(op) + 3] == '0':
                        state = 1
                        break
                    else:
                        continue
                else:
                    start = sub_s.find(op) + len(op) + 3
                    ssub_s = sub_s[start:]
                    end = ssub_s.find(',')
                    obj.append(ssub_s[0:end])
            if state == 1:
                break
            objs.append(obj)
        return objs

    def draw_objs(self, info_str, cfg):
        obj_parameter = cfg.obj_parameter
        objs = self.get_obj_info(info_str, obj_parameter)

        for obj in objs:
            p0 = np.array([-float(obj[1]), float(obj[0])])
            Alpha = float(obj[5])
            length = float(obj[2])
            width = float(obj[3])
            height = float(obj[4])
            Beta = np.arctan((width/2) / (length/2))
            L = math.sqrt(pow(width/2, 2)+pow(length/2, 2))

            # Adjust the target heading angle (relative to the self-vehicle)
            if Alpha >= 0.1:  # left
                if Alpha <= Beta:
                    p1 = np.array([p0[0] + L * np.cos(np.pi / 2 - (-Alpha + Beta)),
                                   p0[1] + L * np.sin(np.pi / 2 - (-Alpha + Beta))])
                else:
                    p1 = np.array([p0[0] + L * np.cos(np.pi / 2 - (Alpha - Beta)),
                                   p0[1] + L * np.sin(np.pi / 2 - (Alpha - Beta))])
                p2 = np.array(
                    [p0[0] + L * np.cos(np.pi / 2 + (Alpha + Beta)), p0[1] + L * np.sin(np.pi / 2 + (Alpha + Beta))])

            elif Alpha <= -0.1:  # right
                Alpha = -Alpha
                p1 = np.array([p0[0]+L*np.sin(Alpha+Beta), p0[1]+L*np.cos(Alpha+Beta)])
                p2 = np.array([p0[0]+L*np.sin(Alpha - Beta), p0[1] +L*np.cos(Alpha - Beta)])

            else:
                p1 = np.array([p0[0] + width / 2, p0[1] + length / 2])
                p2 = np.array([p0[0] - width / 2, p0[1] + length / 2])

            p3 = np.array([2 * p0[0] - p1[0], 2 * p0[1] - p1[1]])
            p4 = np.array([2 * p0[0] - p2[0], 2 * p0[1] - p2[1]])

            # Display type above the target
            glColor4f(0.0, 0.0, 1.0, 1.0)
            glRasterPos3f(p0[0], p0[1], 3)
            s = cfg.obj_class[int(obj[6])]
            for c in s:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))

            # Start drawing the target
            glColor4f(0.6, 0.6, 0.6, 1.0)
            glBegin(GL_QUADS)

            # Bottom
            glVertex3f(p1[0], p1[1], 0.1)
            glVertex3f(p2[0], p2[1], 0.1)
            glVertex3f(p3[0], p3[1], 0.1)
            glVertex3f(p4[0], p4[1], 0.1)

            # Top
            glVertex3f(p1[0], p1[1], 0.1+height)
            glVertex3f(p2[0], p2[1], 0.1+height)
            glVertex3f(p3[0], p3[1], 0.1+height)
            glVertex3f(p4[0], p4[1], 0.1+height)

            # Front
            glVertex3f(p1[0], p1[1], 0.1)
            glVertex3f(p2[0], p2[1], 0.1)
            glVertex3f(p2[0], p2[1], 0.1+height)
            glVertex3f(p1[0], p1[1], 0.1+height)

            # Rear
            glVertex3f(p3[0], p3[1], 0.1)
            glVertex3f(p4[0], p4[1], 0.1)
            glVertex3f(p4[0], p4[1], 0.1+height)
            glVertex3f(p3[0], p3[1], 0.1+height)

            # Left
            glVertex3f(p2[0], p2[1], 0.1)
            glVertex3f(p3[0], p3[1], 0.1)
            glVertex3f(p3[0], p3[1], 0.1+height)
            glVertex3f(p2[0], p2[1], 0.1+height)

            # right
            glVertex3f(p1[0], p1[1], 0.1)
            glVertex3f(p4[0], p4[1], 0.1)
            glVertex3f(p4[0], p4[1], 0.1+height)
            glVertex3f(p1[0], p1[1], 0.1+height)

            glEnd()

    def drwa_obj(self):
        x0, x1 = self.x0, self.x1
        x = x1[0] - x0[0]
        y = x1[1] - x0[1]

        glBegin(GL_QUADS)
        glColor4f(1.0, 0.0, 1.0, 1.0)

        # bottom
        glVertex3f(x0[0], x0[1], x0[2])
        glVertex3f(x0[0], x1[1], x0[2])
        glVertex3f(x1[0], x1[1], x0[2])
        glVertex3f(x1[0], x0[1], x0[2])

        # top
        glVertex3f(x0[0], x0[1], x1[2])
        glVertex3f(x0[0], x1[1], x1[2])
        glVertex3f(x1[0], x1[1], x1[2])
        glVertex3f(x1[0], x0[1], x1[2])

        # left
        glVertex3f(x0[0], x0[1], x0[2])
        glVertex3f(x0[0], x0[1], x1[2])
        glVertex3f(x0[0], x1[1], x1[2])
        glVertex3f(x0[0], x1[1], x0[2])

        # right
        glVertex3f(x1[0], x0[1], x0[2])
        glVertex3f(x1[0], x0[1], x1[2])
        glVertex3f(x1[0], x1[1], x1[2])
        glVertex3f(x1[0], x1[1], x0[2])

        # front
        glVertex3f(x0[0], x0[1], x0[2])
        glVertex3f(x0[0], x0[1], x1[2])
        glVertex3f(x1[0], x0[1], x1[2])
        glVertex3f(x1[0], x0[1], x0[2])

        # Tail
        glVertex3f(x0[0], x1[1], x0[2])
        glVertex3f(x0[0], x1[1], x1[2])
        glVertex3f(x1[0], x1[1], x1[2])
        glVertex3f(x1[0], x1[1], x0[2])

        glEnd()


