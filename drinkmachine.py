from gpiozero import OutputDevice
import time
import threading

class DrinkMachine:

    def __init__(self, pump_one_pin, pump_two_pin, flow_rate):
        self.__pump_one = OutputDevice(pump_one_pin)
        self.__pump_two = OutputDevice(pump_two_pin)
        self.__flow_rate = flow_rate
        self.__current_drink = None
        self.__drink_thread = None

    def drink_process(self):
       	self.__pump_one.on()
	self.__pump_two.on()
        
	pump_one_time = self.__current_drink.pump_one / self.__flow_rate
	pump_two_time = self.__current_drink.pump_two / self.__flow_rate

	shortest_pump_time = min(pump_one_time, pump_two_time) 
	longest_pump_time = max(pump_one_time, pump_two_time)

	shortest_pump = self.__pump_one if pump_one_time == shortest_pump_time else self.__pump_two 
	
	longest_pump = self.__pump_one if shortest_pump == self.__pump_two else self.__pump_two
	
	time.sleep(shortest_pump_time)
	shortest_pump.off()

	time.sleep(max(0, longest_pump_time - shortest_pump_time))
	longest_pump.off()

	self.__current_drink = None	


    def make_drink(self, drink):

        if self.__current_drink != None:
            return "Already making drink! Try again later."

        self.__current_drink = drink

        self.__drink_thread = threading.Thread(target=self.drink_process)
        self.__drink_thread.start()
       
	return "Drink Started"

    def current_drink_progress(self):
        return 'pouring' if self.__drink_thread != None and self.__drink_thread.is_alive() else 'Machine is Free'
