FROM ros:galactic

RUN apt-get update && apt-get install -y && apt-get upgrade -y \
    && apt install python3-vcstool \
    && apt-get install -y git \
    && apt-get -y install python3-pip \
    && python3 -m pip install ruamel.yaml

ARG DEBIAN_FRONTEND=noninteractive
ENV ros2_ws=root/mobilerobot_ws
RUN mkdir -p $ros2_ws/src
WORKDIR $ros2_ws/src

RUN git clone https://github.com/swarmBots-ipa/multirobot_navigation_sim.git \
    && cd multirobot_navigation_sim/path_planner_server/config \
    && chmod +x utils.py \
    && python3 utils.py

RUN . /opt/ros/galactic/setup.sh 
RUN rosdep update
RUN cd ~/mobilerobot_ws \
    && rosdep install --from-paths src --ignore-src -r -y \
    && apt install ros-galactic-gazebo-ros-pkgs -y \
    && apt install ros-galactic-rviz2 -y \
    && echo "Dependecies are installed in the workspace"

RUN cd ~/mobilerobot_ws \
    && . /opt/ros/galactic/setup.sh \
    && colcon build --symlink-install \
    && rm -rf /var/lib/apt/lists/* \
    &&  . install/setup.sh \
    && echo "Building packages completed"


COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"] 
CMD ["bash"]