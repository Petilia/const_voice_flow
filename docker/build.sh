#!/bin/bash

yellow=`tput setaf 3`
reset_color=`tput sgr0`

ARCH="$(uname -m)"

main () {
    docker build . \
        --build-arg UID=$(id -u) \
        --build-arg GID=$(id -g) \
        --build-arg NUM_THREADS=${NUM_THREADS} \
        -t ${ARCH}/const_voice_flow:latest
    popd;
}

main "$@"; exit;