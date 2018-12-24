
class DrinkMachine:

    def __init__(self):
        self.__current_drink = None

    def make_drink(self, drink):

        if self.__current_drink != None:
            return "Already making drink! Try again later."

        self.__current_drink = drink

        return "Drink Started"

    def current_drink_progress(self):
        return "75 %" if self.__current_drink != None else "Machine is Free"