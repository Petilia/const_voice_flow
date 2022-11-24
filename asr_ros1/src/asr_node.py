#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import re

#asr tools
from speeckit_tools import asr_from_yandex_speeckit
from pyaudio_tools import listen_n_seconds, get_device_index

index_device = get_device_index()
FOLDER_ID = "b1gami13b761380nb5hb" # Идентификатор каталога
API_KEY = "AQVN3XofRyHEW5PJOhBYCiObnGaZNYM8IvAQskdp" # API-ключ


def create_random_image():
    rospy.init_node('ASR_node')
    pub_asr = rospy.Publisher('asr_result', String, queue_size=10)

    while not rospy.is_shutdown():
        msg = String()
        listen_n_seconds(index_device, base_folder="/home/appuser/catkin_ws/src/asr_ros1/asr_ros1/src/")
        asr_result = asr_from_yandex_speeckit(FOLDER_ID, API_KEY, base_folder="/home/appuser/catkin_ws/src/asr_ros1/asr_ros1/src/")
        asr_result = asr_result.lower()
        is_go = re.search("поехали|проехали", asr_result)
        if is_go:
            msg.data = "поехали"
        else:
            msg.data = "стоим"

        print(f"result_asr = {asr_result}; to_topic = {msg.data}")
        pub_asr.publish(msg)
      

if __name__ == '__main__':
    try:
        create_random_image()
    except rospy.ROSInterruptException: pass
