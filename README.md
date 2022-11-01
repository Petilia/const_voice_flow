# build image
cd docker  
./build.sh

# Подключение микофона
Сначала подключаемм миикрофон в USB-разъем  
Только после этого запускаем контейнер:  
./start.sh  

# Внутри контейнера:  
Вывести список подключенных устройств - среди них должен быть Plantronics Callisto: 
python py_files/check_devices.py   
Запуск прослушки/распознавания/запросов в dream:  
python py_files/listener.py