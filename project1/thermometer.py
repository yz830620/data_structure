"""
Objective: file for practice List/Array
Date: 2021/12/4
Author: Even Pan
"""

class Thermometer:
    """class for counting temperture"""
    def __init__(self):
        self.tempertures = self._get_temp()

    def _get_temp(self):
        day = 1
        all_temps = []
        while True:
            temp_inp = input(f'What is the highest temperture for Day {day}? ')
            if temp_inp:
                temp_int = int(temp_inp)
                all_temps.append(temp_int)
                day += 1
            else:
                break
        return all_temps

    def count_avg(self):
        return sum(self.tempertures)/len(self.tempertures)

    def count_over_temp(self):
        avg = self.count_avg()
        counter = 0
        for temp in self.tempertures:
            if temp > avg:
                counter += 1
        return counter

if __name__ == "__main__":
    ther = Thermometer()
    print('avg temp: ',ther.count_avg())
    print('days over avg: ',ther.count_over_temp())