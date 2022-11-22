#!/usr/bin/env python3
import os
from ruamel import yaml

current_path = os.getcwd()

barista_0_bt = 'barista_0_bt_navigator.yaml'
barista_1_bt = 'barista_1_bt_navigator.yaml'
barista_2_bt = 'barista_2_bt_navigator.yaml'
barista_3_bt = 'barista_3_bt_navigator.yaml'

with open(barista_0_bt, 'r') as f0:
    data_0 = yaml.load(f0, Loader=yaml.RoundTripLoader) 

with open(barista_1_bt, 'r') as f1:
    data_1 = yaml.load(f1, Loader=yaml.RoundTripLoader) 

with open(barista_2_bt, 'r') as f2:
    data_2 = yaml.load(f2, Loader=yaml.RoundTripLoader) 

with open(barista_3_bt, 'r') as f3:
    data_3 = yaml.load(f3, Loader=yaml.RoundTripLoader) 

dq_string = yaml.scalarstring.DoubleQuotedScalarString

current_bt_path_0 = current_path+"/behavior.xml"
current_bt_path_1 = current_path+"/behavior.xml"
current_bt_path_2 = current_path+"/behavior.xml"
current_bt_path_3 = current_path+"/behavior.xml"

data_0['barista_0/bt_navigator']['ros__parameters']['default_nav_to_pose_bt_xml'] = dq_string(current_bt_path_0)
data_1['barista_1/bt_navigator']['ros__parameters']['default_nav_to_pose_bt_xml'] = dq_string(current_bt_path_1)
data_2['barista_2/bt_navigator']['ros__parameters']['default_nav_to_pose_bt_xml'] = dq_string(current_bt_path_2)
data_3['barista_3/bt_navigator']['ros__parameters']['default_nav_to_pose_bt_xml'] = dq_string(current_bt_path_3)

with open(barista_0_bt, "w") as f0:
    yaml.dump(data_0, f0, Dumper=yaml.RoundTripDumper)

with open(barista_1_bt, "w") as f1:
    yaml.dump(data_1, f1, Dumper=yaml.RoundTripDumper)

with open(barista_2_bt, "w") as f2:
    yaml.dump(data_2, f2, Dumper=yaml.RoundTripDumper)

with open(barista_3_bt, "w") as f3:
    yaml.dump(data_3, f3, Dumper=yaml.RoundTripDumper)