# 1. Создать класс TrafficLight (светофор).
# определить у него один приватный атрибут color (цвет) и метод get_current_signal() (получить текущий цвет);
# после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью: красный (3 сек),
# жёлтый (1 сек), зелёный (3 сек);
# переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
# проверить переключение режимов работы светофора, опрашивая в цикле текущее состояние светофора
# с интервалом 0.5 секунды, используя метод get_current_signal().

from time import sleep
import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def get_current_signal(self):
        start = time.perf_counter()
        print(start)
        if start % 7 < 3:
            return self.__color[0]
        elif 3 < start % 7 < 4:
            return self.__color[1]
        elif 4 < start % 7 < 7:
            return self.__color[2]


a = TrafficLight()

for i in range(20):
    print(a.get_current_signal())
    sleep(0.5)
