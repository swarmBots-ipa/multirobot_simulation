## Mapping the environment
Use only one robot to map the area.
```
ros2 launch barista_gazebo main_one_robots.launch.xml

ros2 run teleop_twist_keyboard teleop_twist_keyboard cmd_vel:=barista_1/cmd_vel

```
## Save maps after creating maps using cartographer_slam
````
ros2 run nav2_map_server map_saver_cli -f empty_room
````