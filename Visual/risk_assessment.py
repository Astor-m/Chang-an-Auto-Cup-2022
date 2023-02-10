from config import *


class Assessment:
    def __init__(self):
        pass

    # Gradient distribution function
    # Define the partial small trapezoidal distribution function
    def belong_function_small(self, x, a, b):
        if x <= a: return 1
        if x >= b: return 0
        return (b - x) / (b - a)

    # Define the skewed large trapezoidal distribution function
    def belong_function_large(self, x, a, b):
        if x <= a: return 0
        if x >= b: return 1
        return (x - a) / (b - a)

    # Define the medium-sized trapezoidal distribution function
    def belong_function_middle(self, x, a, b, c):
        if x <= a and x >= 0: return 0
        if x > a and x <= b: return (x - a) / (b - a)
        if x > b and x < c: return (c - x) / (c - b)
        if x >= c: return 0

    # Generate the scene complexity affiliation matrix R, R1, R2, R3
    def GenomplexityR(self, data):
        R_num_obj = np.array([self.belong_function_small(data['num_obj'], 3, 7),
                              self.belong_function_middle(data['num_obj'], 3, 7, 13),
                              self.belong_function_large(data['num_obj'], 7, 17)
                              ])
        R_obj_complexity = np.array([self.belong_function_small(data['obj_complexity'], 1, 2),
                                     self.belong_function_middle(data['obj_complexity'], 1, 2, 3),
                                     self.belong_function_large(data['obj_complexity'], 2, 3)
                                     ])
        R_pedestrian_percentage = np.array([self.belong_function_small(data['pedestrian_percentage'], 0.15, 0.41),
                                            self.belong_function_middle(data['pedestrian_percentage'], 0.15, 0.41, 0.82),
                                            self.belong_function_large(data['pedestrian_percentage'], 0.41, 0.82)
                                            ])
        R_nonemotor_percentage = np.array([self.belong_function_small(data['nonemotor_percentage'], 0.134, 0.255),
                                           self.belong_function_middle(data['nonemotor_percentage'], 0.134, 0.255, 0.479),
                                           self.belong_function_large(data['nonemotor_percentage'], 0.255, 0.479)
                                           ])
        R_truck_percentage = np.array([self.belong_function_small(data['truck_percentage'], 0.01, 0.2),
                                       self.belong_function_middle(data['truck_percentage'], 0.01, 0.2, 0.45),
                                       self.belong_function_large(data['truck_percentage'], 0.2, 0.45)
                                       ])
        R_mean_curve = np.array([self.belong_function_small(abs(data['mean_curve']), 0.0013, 0.013),
                                 self.belong_function_middle(abs(data['mean_curve']), 0.0013, 0.013, 0.04),
                                 self.belong_function_large(abs(data['mean_curve']), 0.013, 0.04)
                                 ])
        R_lane_slope = np.array([self.belong_function_small(abs(data['lane_slope']), 0.704, 1.67),
                                 self.belong_function_middle(abs(data['lane_slope']), 0.704, 1.67, 3.01),
                                 self.belong_function_large(abs(data['lane_slope']), 1.67, 3.01)
                                 ])
        R_lane_type = np.array([self.belong_function_small(data['lane_type'], 0, 1),
                                self.belong_function_middle(data['lane_type'], 0, 1, 2),
                                self.belong_function_large(data['lane_type'], 1, 2)
                                ])
        R_num_lane_connectivity = np.array([self.belong_function_small(data['num_lane_connectivity'], 1, 2),
                                            self.belong_function_middle(data['num_lane_connectivity'], 1, 2, 4),
                                            self.belong_function_large(data['num_lane_connectivity'], 2, 4)
                                            ])
        R_traffic_sign_complex = np.array([self.belong_function_small(data['traffic_sign_complex'], 3.2, 7.74),
                                           self.belong_function_middle(data['traffic_sign_complex'], 3.22, 7.74, 15),
                                           self.belong_function_large(data['traffic_sign_complex'], 7.74, 15)
                                           ])
        R_lan_arrow = np.array([data['lan_arrow'] == 0,
                                0,
                                data['lan_arrow'] == 1,
                                ]) + 0
        R_ground_markings = np.array([data['ground_markings'] == 0,
                                      0,
                                      data['ground_markings'] == 1,
                                      ]) + 0
        R_split_merge = np.array([data['split_merge'] == 0,
                                  data['split_merge'] == 1,
                                  data['split_merge'] == 2,
                                  ]) + 0
        R_is_in_tunnel = np.array([data['is_in_tunnel'] == 0,
                                   0,
                                   data['is_in_tunnel'] == 1,
                                   ]) + 0
        R_is_in_toll_booth = np.array([data['is_in_toll_booth'] == 0,
                                       0,
                                       data['is_in_toll_booth'] == 1,
                                       ])
        R_is_in_certified_road = np.array([data['is_in_certified_road'] == 0,
                                           0,
                                           data['is_in_certified_road'] == 1,
                                           ])
        R_motion_state_percentage = np.array([self.belong_function_small(data['motion_state_percentage'], 0.1, 0.4),
                                              self.belong_function_middle(data['motion_state_percentage'], 0.1, 0.4, 0.6),
                                              self.belong_function_large(data['motion_state_percentage'], 0.4, 0.6)
                                              ])
        R_type_complex = np.array([self.belong_function_small(data['type_complex'], 10, 30),
                                   self.belong_function_middle(data['type_complex'], 10, 30, 50),
                                   self.belong_function_large(data['type_complex'], 30, 50)
                                   ])
        R1 = np.array(
            [R_num_obj, R_obj_complexity, R_pedestrian_percentage, R_nonemotor_percentage, R_truck_percentage])
        R2 = np.array([R_mean_curve, R_lane_slope, R_lane_type, R_num_lane_connectivity,
                       R_traffic_sign_complex, R_lan_arrow, R_ground_markings, R_split_merge])
        R3 = np.array(
            [R_is_in_tunnel, R_is_in_toll_booth, R_is_in_certified_road, R_motion_state_percentage, R_type_complex])

        return R1, R2, R3

    # Generate R1 affiliation matrix
    def GenDangerR1(self, obj_nums, avg_volectiys, avg_accelerations, avg_distences, avg_volumes):
        R_obj_nums = np.array([self.belong_function_small(obj_nums, 2, 4),
                               self.belong_function_middle(obj_nums, 2, 4, 6),
                               self.belong_function_middle(obj_nums, 4, 6, 11),
                               self.belong_function_middle(obj_nums, 6, 11, 15),
                               self.belong_function_large(obj_nums, 11, 15)
                               ])
        R_avg_volectiys = np.array([self.belong_function_small(avg_volectiys, 2, 8),
                                    self. belong_function_middle(avg_volectiys, 2, 8, 14),
                                    self.belong_function_middle(avg_volectiys, 8, 14, 16),
                                    self.belong_function_middle(avg_volectiys, 14, 16, 25),
                                    self.belong_function_large(avg_volectiys, 16, 25)
                                    ])
        R_avg_accelerations = np.array([self.belong_function_small(avg_accelerations, 0.094, 0.341),
                                        self.belong_function_middle(avg_accelerations, 0.094, 0.341, 0.987),
                                        self.belong_function_middle(avg_accelerations, 0.341, 0.987, 1.722),
                                        self.belong_function_middle(avg_accelerations, 0.987, 1.722, 2.513),
                                        self.belong_function_large(avg_accelerations, 1.722, 2.513)
                                        ])
        R_avg_distences = np.array([self.belong_function_large(avg_distences, 50.58, 71.23),
                                    self.belong_function_middle(avg_distences, 37.69, 50.58, 71.23),
                                    self.belong_function_middle(avg_distences, 19.62, 37.69, 50.58),
                                    self.belong_function_middle(avg_distences, 15.66, 19.62, 37.69),
                                    self.belong_function_small(avg_distences, 15.66, 19.62)
                                    ])
        R_avg_volumes = np.array([self.belong_function_small(avg_volumes, 10, 17),
                                  self.belong_function_middle(avg_volumes, 10, 17, 23),
                                  self.belong_function_middle(avg_volumes, 17, 23, 69),
                                  self.belong_function_middle(avg_volumes, 23, 69, 85),
                                  self.belong_function_large(avg_volumes, 69, 85)
                                  ])
        return np.array([R_obj_nums, R_avg_volectiys, R_avg_accelerations, R_avg_distences, R_avg_volumes])

    # Generate R2 affiliation matrix
    def GenDangerR2(self, speedings, speed, yaw_rate, long_accel, lat_accel, steering_angle):
        R_speedings = np.array([not speedings, 0, 0, 0, speedings]) + 0
        R_speed = np.array([self.belong_function_small(speed, 10, 30),
                            self.belong_function_middle(speed, 10, 30, 50),
                            self.belong_function_middle(speed, 30, 50, 70),
                            self.belong_function_middle(speed, 50, 70, 90),
                            self.belong_function_large(speed, 70, 90)
                            ])
        R_yaw_rate = np.array([self.belong_function_small(yaw_rate, 0.25, 1.57),
                               self.belong_function_middle(yaw_rate, 0.25, 1.57, 4.25),
                               self.belong_function_middle(yaw_rate, 1.57, 4.25, 8.26),
                               self.belong_function_middle(yaw_rate, 4.25, 8.26, 14.57),
                               self.belong_function_large(yaw_rate, 8.26, 14.57)
                               ])
        R_long_accel = np.array([self.belong_function_small(long_accel, 0.25, 0.48),
                                 self.belong_function_middle(long_accel, 0.25, 0.48, 0.96),
                                 self.belong_function_middle(long_accel, 0.48, 0.96, 1.56),
                                 self.belong_function_middle(long_accel, 0.96, 1.56, 2),
                                 self.belong_function_large(long_accel, 1.56, 2)
                                 ])
        R_lat_accel = np.array([self.belong_function_small(lat_accel, 0.131, 0.226),
                                self.belong_function_middle(lat_accel, 0.131, 0.226, 0.733),
                                self.belong_function_middle(lat_accel, 0.226, 0.733, 1.396),
                                self.belong_function_middle(lat_accel, 0.733, 1.396, 2.062),
                                self.belong_function_large(lat_accel, 1.396, 2.062)
                                ])
        R_steering_angle = np.array([self.belong_function_small(steering_angle, 2.84, 7.12),
                                     self.belong_function_middle(steering_angle, 2.84, 7.12, 19.44),
                                     self.belong_function_middle(steering_angle, 7.12, 19.44, 60),
                                     self.belong_function_middle(steering_angle, 19.44, 60, 127.46),
                                     self.belong_function_large(steering_angle, 60, 127.46)
                                     ])
        return np.array([R_speedings, R_speed, R_yaw_rate, R_long_accel, R_lat_accel, R_steering_angle])

    # Generate R3 affiliation matrix
    def GenDangerR3(self, mean_curve, road_type, lane_type, is_in_tunnel):
        R_mean_curve = np.array([self.belong_function_small(mean_curve, 0.001, 0.002),
                                 self.belong_function_middle(mean_curve, 0.001, 0.002, 0.005),
                                 self.belong_function_middle(mean_curve, 0.002, 0.005, 0.02),
                                 self.belong_function_middle(mean_curve, 0.005, 0.02, 0.04),
                                 self.belong_function_large(mean_curve, 0.02, 0.04)
                                 ])
        R_road_type = np.array([road_type == 3, 0, road_type == 1, 0, road_type == 2]) + 0
        R_lane_type = np.array([lane_type == 0, lane_type == 1, lane_type == 2, lane_type == 3, lane_type == 4]) + 0
        R_is_in_tunnel = np.array([not is_in_tunnel, 0, 0, 0, is_in_tunnel]) + 0

        return np.array([R_mean_curve, R_road_type, R_lane_type, R_is_in_tunnel])

    # Get all scene load level element data
    def getOneSceneComplexityElements(self, data):
        # Initialization results
        result = {}
        keys = ['num_obj', 'obj_complexity', 'pedestrian_percentage', 'nonemotor_percentage',
                'truck_percentage', 'mean_curve', 'lane_slope', 'lane_type', 'num_lane_connectivity',
                'traffic_sign_complex', 'lan_arrow', 'ground_markings', 'split_merge', 'is_in_tunnel',
                'is_in_toll_booth', 'is_in_certified_road', 'motion_state_percentage', 'type_complex'
                ]
        for key in keys:
            result[key] = []

        # Obtain target detection elements
        num_obj = 0
        obj_complexity = 0
        pedestrian_percentage = 0
        nonemotor_percentage = 0
        truck_percentage = 0
        obj_class = []
        objs = eval(data['objs/fus_objs'])
        for obj in objs:
            if objs[obj]['track_id'] == 0:  continue
            num_obj += 1
            obj_class.append(objs[obj]['classification'])

        # Statistical target detection elements
        obj_complexity = len(set(obj_class))
        if num_obj != 0:
            pedestrian_percentage = obj_class.count(4) / len(obj_class)
            nonemotor_percentage = (obj_class.count(5) + obj_class.count(8) + obj_class.count(9)) / len(obj_class)
            truck_percentage = (obj_class.count(2) + obj_class.count(7)) / len(obj_class)

        # Obtain road condition elements
        link_list = eval(data['link_list/hdmap'])

        mean_curve = 0
        lane_slope = 0
        lane_type = 0
        num_lane_connectivity = 0
        traffic_sign_complex = 0
        lan_arrow = 0
        ground_markings = 0
        split_merge = 0
        vehicle_pos_current_link_id = data['vehicle_pos_current_link_id/hdmap']
        vehicle_pos_current_lane = data['vehicle_pos_current_lane_num/hdmap']
        link_list_key = 'links_0'
        lane_list_key = 'lane_attributelists_' + str(vehicle_pos_current_lane)
        for link_key in link_list:
            if link_list[link_key]['link_id'] == vehicle_pos_current_link_id:
                link_list_key = link_key

        if link_list_key in link_list.keys():
            if lane_list_key in link_list[link_list_key]['lane_attributelists'].keys():
                mean_curve = data['lane_curvature_100m/hdmap']
                if len(link_list[link_list_key]['lane_attributelists'][lane_list_key]['lane_slope_list']) != 0:
                    lane_slope = link_list[link_list_key]['lane_attributelists'][lane_list_key]['lane_slope_list'][
                        'lane_slope_list_0']['value']
                lane_type = link_list[link_list_key]['type']
                num_lane_connectivity = len(
                    link_list[link_list_key]['lane_attributelists'][lane_list_key]['lane_connectivity_list'])
                traffic_sign_complex = len(link_list[link_list_key]['traffic_info'])
                if len(link_list[link_list_key]['lane_attributelists'][lane_list_key]['lane_arrows']) != 0:
                    lan_arrow = link_list[link_list_key]['lane_attributelists'][lane_list_key]['lane_arrows']  #
                if len(link_list[link_list_key]['ground_markings']) != 0:  #
                    ground_markings = link_list[link_list_key]['ground_markings']['ground_markings_0']['type']
                if len(link_list[link_list_key]['split_merge_list']) != 0:
                    split_merge = len(link_list[link_list_key]['split_merge_list'])  #

        # Acquisition of environmental elements
        points = eval(data['points/freespace_fc'])
        is_in_tunnel = 0
        is_in_toll_booth = 0
        is_in_certified_road = 0
        type_complex = 0
        motion_state_percentage = 0
        motion_state_class = []
        type_class = []
        if link_list_key in link_list.keys():
            if lane_list_key in link_list[link_list_key]['lane_attributelists'].keys():
                is_in_tunnel = link_list[link_list_key]['is_in_tunnel']
                is_in_toll_booth = link_list[link_list_key]['is_in_toll_booth']
                is_in_certified_road = link_list[link_list_key]['is_in_certified_road']
        for point_key in points:
            motion_state_class.append(points[point_key]['motion_state'])
            type_class.append(points[point_key]['type'])

        type_complex = len(set(type_class))
        motion_state_percentage = motion_state_class.count(1) / len(motion_state_class)
        # Add all results to results
        for key in keys:
            result[key] = eval(key)

        return result

    # Traffic elements
    def traficElements(self, data):
        objs = eval(data['objs/fus_objs'])
        num_obj = 0
        avg_velocity = 0
        avg_acceleration = 0
        avg_distence = 0
        avg_volume = 0
        for key in objs:
            if objs[key]['track_id'] == 0:  continue
            num_obj += 1
            avg_velocity += math.sqrt(
                (objs[key]['lateral_absolute_velocity'] ** 2 + objs[key]['longitudinal_absolute_velocity'] ** 2))
            avg_acceleration += math.sqrt(
                objs[key]['longitudinal_absolute_acceleration'] ** 2 + objs[key]['lateral_absolute_acceleration'] ** 2)
            avg_distence += math.sqrt(objs[key]['longitudinal_distance'] ** 2 + objs[key]['lateral_distance'] ** 2)
            avg_volume += objs[key]['length'] * objs[key]['width'] * objs[key]['heigh']
        if num_obj == 0:
            return 0, 0, 0, 0, 0
        return num_obj, avg_velocity / num_obj, avg_acceleration / num_obj, avg_distence / num_obj, avg_volume / num_obj

    # Self-vehicle movement elements
    def stpMotionElements(self, data):
        vehicle_speed = data['esp_vehicle_speed/stp_motion']
        long_accel = data['esp_long_accel/stp_motion']
        lat_accel = data['esp_lat_accel/stp_motion']
        steering_angle = data['sas_steering_angle/stp_motion']
        yaw_rate = data['esp_yaw_rate/stp_motion']
        hdmap_static = eval(data['link_list/hdmap'])
        current_link_id = data['vehicle_pos_current_link_id/hdmap']
        for link in hdmap_static:
            if current_link_id == hdmap_static[link]['link_id']:
                speed_limit = hdmap_static[link]['lane_attributelists']['lane_attributelists_0']['speed_limit_value']
                break
        speeding = 0
        if vehicle_speed > speed_limit:
            speeding = 1
        return speeding, vehicle_speed, yaw_rate, long_accel, lat_accel, steering_angle

    def sceneDangerAnalysis(self, data, describe=False):
        """This function analyzes the level of danger of the current driving scenario based on the input data.

         Given one of the rows of data in the example.csv file, the function uses hierarchical analysis
         the weight of the current road to return the degree of danger, where the judgment matrix A, A1, A2, A3 data are
         obtained in the data analysis section.

         :param data: one of the rows of the example.csv data file
         :type pandas.core.series.
         :param describe: whether to describe the data
         :type bool
         :returns: Returns the current driving scenario as a hazard level (1-5)
         """
        # Driving scenario hazard level definition
        V = np.array([5, 4, 3, 2, 1])
        # Judgment matrix 𝐴, and the corresponding weight values
        A = np.array([0.260497956, 0.63334572, 0.106156324])
        # Judgment matrix 𝐴1, and the corresponding weight values
        A1 = np.array([0.440911506, 0.094912103, 0.206314639, 0.194393289, 0.063468463])
        # Judgment matrix 𝐴2, and the corresponding weight values
        A2 = np.array([0.454977804, 0.236007634, 0.153610166, 0.075172903, 0.052930621, 0.027300873])
        # Judgment matrix 𝐴3, and the corresponding weight values
        A3 = np.array([0.070641858, 0.131505994, 0.53794955, 0.259902597])
        # Access to evaluation metrics
        obj_nums, avg_volectiys, avg_accelerations, avg_distences, avg_volumes = self.traficElements(data)
        speedings, speed, yaw_rate, long_accel, lat_accel, steering_angle = self.stpMotionElements(data)
        mean_curve, road_type, lane_type, is_in_tunnel = self.laneInformationElements(data)

        # Generate the affiliation matrix
        R1 = self.GenDangerR1(obj_nums, avg_volectiys, avg_accelerations, avg_distences, avg_volumes)
        R2 = self.GenDangerR2(speedings, speed, abs(yaw_rate), abs(long_accel), abs(lat_accel), abs(steering_angle))
        R3 = self.GenDangerR3(abs(mean_curve), road_type, lane_type, is_in_tunnel)
        B1 = A1 @ R1
        B2 = A2 @ R2
        B3 = A3 @ R3
        R = np.array([B1, B2, B3])
        B = A @ R
        result = B @ V
        danger_level = 'General'
        if result >= 1 and result < 1.8:
            danger_level = 'High'
        elif result >= 1.8 and result < 2.6:
            danger_level = 'sub_High'
        elif result >= 2.6 and result < 3.4:
            danger_level = 'General'
        elif result >= 3.4 and result < 4.2:
            danger_level = 'sub_Low'
        elif result >= 4.2:
            danger_level = 'Low'

        return danger_level, result

    # Lane Information Elements
    def laneInformationElements(self, data):
        mean_curve = data['lane_curvature_100m/hdmap']
        lane_type, road_type, is_in_tunnel = 0, 0, 0
        current_link_id = data['vehicle_pos_current_link_id/hdmap']
        hdmap_static = eval(data['link_list/hdmap'])
        for link in hdmap_static:
            if current_link_id == hdmap_static[link]['link_id']:
                lane_type = hdmap_static[link]['type']
                road_type = hdmap_static[link]['lane_attributelists']['lane_attributelists_0']['type']
                is_in_tunnel = 0
                if hdmap_static[link]['is_in_tunnel']:
                    is_in_tunnel = 1
                break
        return mean_curve, lane_type, road_type, is_in_tunnel

    def sceneComplexityAnalysis(self, data, describe=False):
        """This function analyzes the complexity of the current driving scenario based on the input data.

        Given one of the rows of data in the example.csv file, the function uses hierarchical analysis
        the weights return the current road hazard level, where the judgment matrix A, A1, A2, A3 data are
        obtained in the data analysis section.

        :param data: one of the rows of the example.csv data file
        :type pandas.core.series.
        :param describe: whether to describe the data
        :type bool
        :returns: returns the complexity of the road in the current driving scenario (level 1-3)
        """
        # Driving scenario hazard level definition
        V = np.array([3, 2, 1])
        # Judgment matrix 𝐴, and the corresponding weight values
        A = np.array([0.63334572, 0.26049796, 0.10615632])
        # Judgment matrix 𝐴1, and the corresponding weight values
        A1 = np.array([0.50337157, 0.22813875, 0.14964124, 0.07250888, 0.04633956])
        # Judgment matrix 𝐴2, and the corresponding weight values
        A2 = np.array([0.06887013, 0.07243021, 0.16498852, 0.14438139, 0.26628435, 0.05814893, 0.17204697, 0.0528495])
        # Judgment matrix 𝐴3, and the corresponding weight values
        A3 = np.array([0.19476275, 0.0849098, 0.06042818, 0.23967572, 0.42022356])
        # Access to evaluation metrics
        judge_data = self.getOneSceneComplexityElements(data)
        # Generate the affiliation matrix
        R1, R2, R3 = self.GenomplexityR(judge_data)
        #     print(R2)
        B1 = A1 @ R1
        B2 = A2 @ R2
        B3 = A3 @ R3
        R = np.array([B1, B2, B3])
        B = A @ R
        result = B @ V
        if describe:
            print('===========================================')
            print(judge_data)
        complexity_level = 'General'
        if result >= 0 and result < 1.4:
            complexity_level = 'Complex'
        elif result >= 1.4 and result < 2.4:
            complexity_level = 'General'
        elif result >= 2.4:
            complexity_level = 'Simple'

        return complexity_level, result

    def risk_info(self, data):
        complexity_level, result_c = self.sceneComplexityAnalysis(data)
        danger_level, result_d = self.sceneDangerAnalysis(data)
        return complexity_level, result_c, danger_level, result_d
