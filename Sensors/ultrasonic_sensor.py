import random
import time

class UltraSonicSensor():
    def __init__(self, number : int = None, trigger_pin : int = None, echo_pin : int = None):
        self.__number = number
        self.__trigger_pin = trigger_pin
        self.__echo_pin = echo_pin
        
    def __get_echo_time(self):
        return round(random.uniform(0.0006, 0.023), 5)
        
    def __calculate_distance(self):
        echo_time = self.__get_echo_time()
        distance = round(343.0*echo_time, 5)/2
        return distance
    
    def get_distance(self):
        for i in range(10):
            distance = self.__calculate_distance()
            print(f"distance from the obj. : {distance} meter")
            time.sleep(0.002)
        return distance
            
        
# Sensor creation and test
sensor_1 = UltraSonicSensor(1, 18, 24)

if __name__ == '__main__':
    try:
        sensor_1.get_distance()
    except KeyboardInterrupt:
        print("left succesfully")