#!/bin/bash

# HOST_PY_DIR=/home/petryashin_ie/YOLOX/train_YOLOX/graffiti/py_files/
# DOCKER_PY_DIR=/home/appuser/py_files/

# HOST_dataset=/mnt/hdd8/Datasets/graffiti/data_margo/
# DOCKER_dataset=/home/appuser/dataset/

# docker run --gpus all -it --rm \
#   --shm-size=8gb --env="DISPLAY"  \
#   -v $HOST_PY_DIR:$DOCKER_PY_DIR  \
#   -v $HOST_dataset:$DOCKER_dataset  \
#   train_yolox


# -v $workspace_dir/../../:/home/docker_trajectronplusplus/catkin_ws/src:rw \
# -v /mnt/hdd8/Datasets/Centerpoint_output_rosbags/:/home/docker_trajectronplusplus/catkin_ws/rosbags:rw \

cd "$(dirname "$0")"

workspace_dir=$PWD

desktop_start() {
    xhost +local:
    docker run -it -d --rm \
        --gpus all \
        --ipc host \
        --network host \
        --env="DISPLAY" \
        --env="QT_X11_NO_MITSHM=1" \
        --privileged \
        --name const_voice_flow \
        --device /dev/snd \
        --group-add=audio \
        -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
        -v $workspace_dir/../py_files/:/home/appuser/py_files:rw \
        ${ARCH}/const_voice_flow:latest
    xhost -
}

# --device /dev/snd:/dev/snd \
# --env ALSA_CARD=Generic \


main () {
   
    ARCH="$(uname -m)"
    desktop_start;
   
}

main;



