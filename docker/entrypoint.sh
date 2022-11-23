#!/bin/bash
set -e 

source /opt/ros/galactic/setup.sh
source ~/mobilerobot_ws/install/setup.sh
exec "$@"