from config import *


class drive_information:
    def __init__(self):
        pass

    # 显示数据
    def draw_text(self, info_str, complexity_level, result_c, danger_level, result_d, EYE):

        glColor4f(0.0, 0.0, 0.0, 0.0)

        Environment = 'Current Environment'
        glRasterPos3f(EYE[0] - 16, EYE[1] + 14, EYE[2] - 5)
        for c in Environment:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
        # ---------------------------------------------------------------------

        ss = 'Self-car situation'
        glRasterPos3f(EYE[0] + 15, EYE[1] + 25, EYE[2] - 5)
        for c in ss:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))

        speed = str(info_str)
        cs = 'Current speed:' + speed[:min(4, len(speed)-1)] + 'km/h'
        glRasterPos3f(EYE[0] + 12, EYE[1] + 20, EYE[2] - 5)
        for c in cs:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))

        cs = 'complexity_level:' + complexity_level + '  ' + str(result_c)[0:5]
        glRasterPos3f(EYE[0] - 14.3, EYE[1] + 12, EYE[2] - 5)
        for c in cs:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))

        cs = 'danger_level:' + danger_level + '  ' + str(result_d)[0:5]
        glRasterPos3f(EYE[0] - 12.7, EYE[1] + 10, EYE[2] - 5)
        for c in cs:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))


