#!/bin/bash

docker exec --user "appuser" -it const_voice_flow \
        /bin/bash -c "source /opt/ros/noetic/setup.bash; cd /home/docker_yolox; /bin/bash"

        
        
