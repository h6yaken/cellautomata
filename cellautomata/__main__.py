#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def advance(car_line, road_length):
    advanced_car_line = [0] * road_length
    num_advanced_car = 0

    for index in range(road_length):
        # 最後の配列の次の車列は、最初になる
        if index == road_length - 1:
            # 車がいない場所の処理は不要
            if not car_line[index]:
                break

            # 前に車がいないとき、1マス前進する
            if not car_line[0]:
                advanced_car_line[0] = car_line[index]
                num_advanced_car += 1
                break

            advanced_car_line[index] = car_line[index]
            break

        # 車がいない場所の処理は不要
        if not car_line[index]:
            continue

        # 前に車がいないとき、1マス前進する
        if not car_line[index + 1]:
            advanced_car_line[index + 1] = car_line[index]
            num_advanced_car += 1
            continue

        advanced_car_line[index] = car_line[index]

    return advanced_car_line, num_advanced_car


def run(road_length, car_num, time):
    # road_lengthの道路(セル)に、CAR_NUM台の車をランダムにセットする
    car_line = [0] * (road_length - car_num) + [1] * car_num
    random.shuffle(car_line)

    sum_amount_flow = 0
    # 車列の間隔が均等になるまでの時間
    await_time = 10
    for var in range(time):
        tmp_car_line = car_line
        return_value = advance(tmp_car_line, road_length)
        car_line = return_value[0]
        if var > (await_time - 1):
            sum_amount_flow += return_value[1]

    amount_flow = sum_amount_flow / (time - await_time)
    return amount_flow


if __name__ == '__main__':
    road_length = 20
    car_num = 15
    # 車列の間隔が均等になるまで待つ必要があるので、20以上を設定する
    time = 100
    print("road_length： " + str(road_length))
    print("car_num    ： " + str(car_num))
    print("time       ： " + str(time) + "\n")

    density = car_num / road_length
    print("density    ： " + str(density))

    repeat_time = 1
    sum_amount_flow = 0
    for var in range(repeat_time):
        sum_amount_flow += run(road_length, car_num, time)
    print("amount_flow： " + str(sum_amount_flow / repeat_time))
