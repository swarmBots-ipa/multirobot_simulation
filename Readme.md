# Multi Robot Simulator for SwarmBot 

![](sim.png)
## Mapping the environment
Use only one robot to map the area and one need to do it only once. 
```
ros2 launch barista_gazebo main_one_robots.launch.xml

ros2 launch cartographer_slam cartographer.launch.py

ros2 run teleop_twist_keyboard teleop_twist_keyboard cmd_vel:=barista_1/cmd_vel

```
## Save maps after creating maps using cartographer_slam
````
ros2 run nav2_map_server map_saver_cli -f empty_room
````

## Bringup the multirobot simulation, Localization and Pathplanning
````
ros2 launch multirobot_bringup multirobot_bringup.launch.xml
````
