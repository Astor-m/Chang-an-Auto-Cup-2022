import time

from config import *
import risk_assessment as r_a

IS_PERSPECTIVE = True  # Perspective Projection
VIEW = np.array([-0.8, 0.8, -0.8, 0.8, 1.0, 100.0])  # The left/right/bottom/top/near/far sides of the view body
SCALE_K = np.array([0.8, 0.8, 0.8])  # Model scaling
EYE = np.array([-1.0, -10.0, 12.0])  # Eye Position
LOOK_AT = np.array([0.0, 0.0, 0.0])  # Reference point for aiming direction (default at the origin of coordinates)
EYE_UP = np.array([0.0, 1.0, 0.0])  # Define above for the observer (default positive direction of the y-axis)
WIN_W, WIN_H = 840, 480  # Save variables for window width and height
LEFT_IS_DOWNED = False  # Left mouse button is pressed
MOUSE_X, MOUSE_Y = 0, 0  # The starting position saved when examining the amount of mouse displacement

data = pd.core.frame.DataFrame()  # Initialization data
data_row = 0  # Read the data_row row of the data


# Adjusting the viewing angle
def getposture():
    global EYE, LOOK_AT

    dist = np.sqrt(np.power((EYE - LOOK_AT), 2).sum())
    if dist > 0:
        phi = np.arcsin((EYE[1] - LOOK_AT[1]) / dist)
        theta = np.arcsin((EYE[0] - LOOK_AT[0]) / (dist * np.cos(phi)))
    else:
        phi = 0.0
        theta = 0.0

    return dist, phi, theta


DIST, PHI, THETA = getposture()


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)  # Turn on depth testing to achieve masking relationships
    glDepthFunc(GL_LEQUAL)  # Set the depth test function


# Obtain information about objects (road surface, lane lines, self-vehicle conditions)
def get_info():
    road = road_condition.road()
    lane_c = line_condition.line()
    color = np.array([0.9, 0.9, 0.9, 1.0])
    own = own_condition.own(color, 1)
    objs = objects.obj()
    info = drive_info.drive_information()
    risk_info = r_a.Assessment()

    return road, lane_c, own, objs, info, risk_info


# Read data, return data and current data row
def read_data():
    global data_row
    global data

    if data_row == 0:
        data = pd.read_csv(cfg.load_data)
        data_row += 1
    else:
        data_row += 1
    return data, data_row-1


# Set window parameters
def set_conf():
    global IS_PERSPECTIVE, VIEW
    global EYE, LOOK_AT, EYE_UP
    global SCALE_K
    global WIN_W, WIN_H

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if WIN_W > WIN_H:
        if IS_PERSPECTIVE:
            glFrustum(VIEW[0] * WIN_W / WIN_H, VIEW[1] * WIN_W / WIN_H, VIEW[2], VIEW[3], VIEW[4], VIEW[5])
        else:
            glOrtho(VIEW[0] * WIN_W / WIN_H, VIEW[1] * WIN_W / WIN_H, VIEW[2], VIEW[3], VIEW[4], VIEW[5])
    else:
        if IS_PERSPECTIVE:
            glFrustum(VIEW[0], VIEW[1], VIEW[2] * WIN_H / WIN_W, VIEW[3] * WIN_H / WIN_W, VIEW[4], VIEW[5])
        else:
            glOrtho(VIEW[0], VIEW[1], VIEW[2] * WIN_H / WIN_W, VIEW[3] * WIN_H / WIN_W, VIEW[4], VIEW[5])

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glScale(SCALE_K[0], SCALE_K[1], SCALE_K[2])

    gluLookAt(
        EYE[0], EYE[1], EYE[2],
        LOOK_AT[0], LOOK_AT[1], LOOK_AT[2],
        EYE_UP[0], EYE_UP[1], EYE_UP[2]
    )

    glViewport(0, 0, WIN_W, WIN_H)


def draw():

    global EYE

    set_conf()  # Set window parameters

    data, data_row = read_data()  # Read the data_row row

    # Determine if data reading is complete
    if data_row == data.shape[0]:
        exit(0)

    road, line_c, own, objs, info, risk_info = get_info()
    complexity_level, result_c, danger_level, result_d = risk_info.risk_info(data.iloc[data_row])
    info.draw_text(data['esp_vehicle_speed/stp_motion'][data_row], complexity_level, result_c, danger_level, result_d, EYE)
    objs.draw_objs(data['objs/fus_objs'][data_row], cfg)
    road.draw_road()
    line_c.draw_lines(data['lines/fus_lines'][data_row], cfg)
    own.draw_own()
    time.sleep(0.3)
    glutSwapBuffers()
    glFlush()


def reshape(width, height):
    global WIN_W, WIN_H
    WIN_W, WIN_H = width, height
    glutPostRedisplay()


# Mouse click event
def mouseclick(button, state, x, y):
    global SCALE_K
    global LEFT_IS_DOWNED
    global MOUSE_X, MOUSE_Y

    MOUSE_X, MOUSE_Y = x, y
    if button == GLUT_LEFT_BUTTON:
        LEFT_IS_DOWNED = state == GLUT_DOWN
    elif button == 3:
        SCALE_K *= 1.05
        glutPostRedisplay()
    elif button == 4:
        SCALE_K *= 0.95
        glutPostRedisplay()


# Mouse click and drag
def mousemotion(x, y):
    global LEFT_IS_DOWNED
    global EYE, EYE_UP
    global MOUSE_X, MOUSE_Y
    global DIST, PHI, THETA
    global WIN_W, WIN_H

    if LEFT_IS_DOWNED:
        dx = MOUSE_X - x
        dy = y - MOUSE_Y
        MOUSE_X, MOUSE_Y = x, y

        PHI += 2 * np.pi * dy / WIN_H
        PHI %= 2 * np.pi
        THETA += 2 * np.pi * dx / WIN_W
        THETA %= 2 * np.pi
        r = DIST * np.cos(PHI)

        EYE[1] = DIST * np.sin(PHI)
        EYE[0] = r * np.sin(THETA)
        EYE[2] = r * np.cos(THETA)

        if 0.5 * np.pi < PHI < 1.5 * np.pi:
            EYE_UP[1] = -1.0
        else:
            EYE_UP[1] = 1.0

        glutPostRedisplay()


def keydown_(key, x, y):
    if key == b' ':  # Spacebar to switch the projection mode
        exit(0)


def keydown(key, x, y):
    global DIST, PHI, THETA
    global EYE, LOOK_AT, EYE_UP
    global IS_PERSPECTIVE, VIEW

    if key in [b'x', b'X', b'y', b'Y', b'z', b'Z']:
        if key == b'x':
            LOOK_AT[0] -= 0.01
        elif key == b'X':
            LOOK_AT[0] += 0.01
        elif key == b'y':
            LOOK_AT[1] -= 0.01
        elif key == b'Y':
            LOOK_AT[1] += 0.01
        elif key == b'z':
            LOOK_AT[2] -= 0.01                                                       
        elif key == b'Z':
            LOOK_AT[2] += 0.01

        DIST, PHI, THETA = getposture()
        glutPostRedisplay()
    elif key == b'\r':  # Enter key, viewpoint advance
        EYE = LOOK_AT + (EYE - LOOK_AT) * 0.9
        DIST, PHI, THETA = getposture()
        glutPostRedisplay()
    elif key == b'\x08':  # Backspace key, viewpoint backward
        EYE = LOOK_AT + (EYE - LOOK_AT) * 1.1
        DIST, PHI, THETA = getposture()
        glutPostRedisplay()
    elif key == b' ':
        IS_PERSPECTIVE = not IS_PERSPECTIVE
        glutPostRedisplay()


def main():
    glutInit()  # Initialize window
    displayMode = GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH
    glutInitDisplayMode(displayMode)

    glutInitWindowSize(WIN_W, WIN_H)
    glutInitWindowPosition(200, 200)
    glutCreateWindow('Visual')

    # Start visualization
    init()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouseclick)
    glutMotionFunc(mousemotion)
    glutKeyboardFunc(keydown)
    glutMainLoop()


if __name__ == "__main__":
    main()