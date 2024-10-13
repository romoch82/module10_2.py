from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        enemy_count = 100
        day_count = 0
        print(f'{self.name}, на нас напали!')
        while enemy_count > 0:
            enemy_count -= self.power
            day_count += 1
            print(f'{self.name} сражается {day_count} дней, осталось {enemy_count} воинов' + '\n')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)!' + '\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()