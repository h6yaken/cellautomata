#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from time import sleep

ROAD_LENGTH = 20
CAR_NUM = 10


def advance(car_line):
    advanced_car_line = [0] * ROAD_LENGTH

    for index in range(ROAD_LENGTH):

        if index == ROAD_LENGTH - 1:
            if not car_line[0]:
                advanced_car_line[0] = car_line[index]
                continue

        # 車がいない場所の処理は不要
        if not car_line[index]:
            continue

        # 前に車がいないとき、1マス前進する
        if not car_line[index + 1]:
            advanced_car_line[index + 1] = car_line[index]
            continue

        advanced_car_line[index] = car_line[index]

    return advanced_car_line


def run():
    # ROAD_LENGTHの道路(セル)に、CAR_NUM台の車をランダムにセットする
    car_line = [0] * (ROAD_LENGTH - CAR_NUM) + [1] * CAR_NUM
    random.shuffle(car_line)
    print(car_line)

    for var in range(10):
        tmp_car_line = car_line
        car_line = advance(tmp_car_line)
        print(car_line)
        sleep(0.5)


if __name__ == '__main__':
    run()
