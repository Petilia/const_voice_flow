# FROM python:3.8
FROM osrf/ros:noetic-desktop-full

ENV DEBIAN_FRONTEND=noninteractive

RUN chmod 1777 /tmp

RUN apt-get update && \
    apt-get -y install --no-install-recommends tzdata && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y --no-install-recommends git \
                       python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update \
        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libsndfile1-dev ffmpeg -y \
        && pip3 install pyaudio

COPY . .

RUN pip3 install -r requirements.txt
RUN pip3 install fastapi uvicorn pydantic
# RUN pip3 install roslibpy

# create a non-root user
ARG USER=appuser
ARG UID=1000
ARG GID=1000
ARG PW=user

RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | chpasswd && adduser ${USER} sudo
WORKDIR /home/${USER}
RUN mkdir -p catkin_ws/src && chown -R ${UID}:${GID} /home/${USER}
RUN chown -R ${UID}:${GID} /home
USER ${UID}:${GID}


