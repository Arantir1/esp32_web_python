# ESP32 CONTROL WEBPAGE (WITH MICROPYTHON)

## Installation

1. Install "esptool" and "ampy" tools:
```
pip3 install esptool
pip3 install adafruit-ampy
```

2. Run erase command:
```
esptool.py --port /dev/ttyUSB0 erase_flash
```

3. Flash ESP32 with OTA firmware:
```
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 firmware_ota_v1.18.bin
```

4. Change "ssid" and "password" variables in `boot.py` file and upload python files into microcontroller
```
ampy -p /dev/ttyUSB0 put ./boot.py
ampy -p /dev/ttyUSB0 put ./main.py
```

5. Now reset device plug-out/plug-in or with next command:
```
ampy -p /dev/ttyUSB0 reset
```
6. To enable debug run command:
```
ampy -p /dev/ttyUSB0 run ./main.py
```

Here you will see output of your python code

Good luck!

