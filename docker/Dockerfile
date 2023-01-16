FROM python:3.8

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libsndfile1-dev ffmpeg -y \
        && pip3 install pyaudio

COPY . .

RUN pip3 install -r requirements.txt
RUN pip3 install fastapi uvicorn pydantic

# create a non-root user
ARG USER=appuser
ARG UID=1000
ARG GID=1000
# default password
ARG PW=user
RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | chpasswd && adduser ${USER} sudo
RUN chown -R ${UID}:${GID} /home
USER ${UID}:${GID}

WORKDIR /home/${USER}
