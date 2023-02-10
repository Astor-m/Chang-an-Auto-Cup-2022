from config import *


class line:
    def __init__(self):
        pass

    # Get lane line type, color, point set
    def get_line_point(self, lines):
        y = np.arange(-4, 41, 4)
        x = []
        color = []
        typee = []
        for line in lines:
            x_ = []
            for y_ in y:
                res = float(line[5]) + float(line[4])*y_ + float(line[3])*pow(y_, 2) + float(line[2])*pow(y_, 3)
                x_.append(res)
            x.append(x_)
            typee.append(line[0])
            color.append(line[1])
        return typee, color, x, y

    # Read lane line parameters
    def get_line_parameter(self, sstr, parameter_name):
        s = sstr
        line = []
        for i in range(6):
            sub_line = []
            sstart = 0
            for pn in parameter_name:
                start = s.rfind(pn) + len(pn) + 3
                if pn == parameter_name[5]:
                    sstart = start
                sub_s = s[start:]
                end = sub_s.find(',')
                parameter = sub_s[0:end]
                sub_line.append(parameter)
            s = s[0:sstart - 5]
            line.append(sub_line)
        return line

    # Drawing lane lines
    def draw_lines(self, info_str, cfg):
        parameter_name = cfg.parameter_name
        lines = self.get_line_parameter(info_str, parameter_name)
        typee, color, x, y = self.get_line_point(lines)

        for p, t, c in zip(x, typee, color):

            pre_point = np.array([0, 0, -1])

            if t == '11':  # Determine if the lane line is valid
                continue

            if p[2] == 0.0 and p[3] == 0.0 and p[4] == 0.0 and p[5] == 0.0:  # Eliminate incorrect lane lines
                continue

            # Draw solid lines
            if t == '0':
                glBegin(GL_LINES)
                glColor4f(1.0, 1.0, 1.0, 1.0)
                glVertex3f(-p[0], y[0], 0.1)
                for x_, y_ in zip(p, y):
                    x_ = -x_
                    glVertex3f(x_, y_, 0.1)
                    glVertex3f(x_, y_, 0.1)
                glVertex3f(-p[11], y[11], 0.1)
                glEnd()

            # Draw dashed lines
            else:
                glBegin(GL_LINES)
                glColor4f(1.0, 1.0, 1.0, 1.0)
                for x_, y_ in zip(p, y):
                    x_ = -x_
                    if x_ == 0:
                        continue
                    glVertex3f(x_, y_, 0.1)
                glEnd()