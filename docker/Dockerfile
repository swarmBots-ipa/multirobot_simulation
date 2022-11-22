FROM ros:galactic

RUN apt-get update && apt-get install -y \
    && apt install python3-vcstool \
    && apt-get install -y git \
    && apt-get -y install python3-pip \
    && python3 -m pip install ruamel.yaml

ENV ros2_ws=root/mobilerobot_ws
RUN mkdir -p $ros2_ws/src
WORKDIR $ros2_ws/src

RUN git clone https://github.com/swarmBots-ipa/multirobot_navigation_sim.git
WORKDIR $ros2_ws/src/multirobot_navigation_sim/path_planner_server/config
RUN chmod +x utils.py \
    && python3 utils.py

WORKDIR $ros2_ws
    
RUN rosdep update \
    && rosdep install --from-paths src --ignore-src -r -y \
    && echo "Dependecies are installed in the workspace"

RUN . /opt/ros/galactic/setup.sh \
    && colcon build \
    && rm -rf /var/lib/apt/lists/* \
    && echo "Building packages completed"


COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"] 
CMD ["bash"]