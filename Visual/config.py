from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math
import time
import string

import own_condition
import objects
import road_condition
import line_condition
import drive_info


class cfg:
    load_data='data/data1.csv'
    parameter_name = ['type', 'color', 'curve_parameter_a3', 'curve_parameter_a2', 'curve_parameter_a1','curve_parameter_a0']  # Lane Line Field
    obj_parameter = ['track_id', 'longitudinal_distance', 'lateral_distance', 'length', 'width', 'heigh','heading_angle', 'classification']  # Target field
    obj_class = ['unknown', 'car', 'truck', 'motorbike', 'person', 'bike', 'bus', 'other', 'trollry', 'column', 'iron bucket', 'locked parking', 'parking']  # Target Category