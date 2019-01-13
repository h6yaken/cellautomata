#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class CarLine():
    def __init__(self, length, num):
        if length < num:
            num = length
            print("[WARNING] length < num. Set num = length")

        # 車列の長さ
        self.length = length
        # 車両の数
        self.num = num
        # Carクラスの入れ物
        self.cars = list()

        self.make_line()

    # 車列をつくる
    def make_line(self):
        self.cars = [Car() for var in range(self.num)]

        # 車の配置はランダムに行う
        locations = [var for var in range(self.length)]
        random_locations = random.sample(locations, self.num)
        for index in range(len(random_locations)):
            self.cars[index].set_location(random_locations[index])

        # 各車のstatusをセットする
        # 前に車がいれば止まっている。いなければ、走っている状態とする

        car_locations = [car.location for car in self.cars]
        for current_car in self.cars:
            if current_car.location == (self.length - 1):
                if 0 in car_locations:
                    current_car.set_status(0)
                    continue

                current_car.set_status(1)

            else:
                if (current_car.location + 1) in car_locations:
                    current_car.set_status(0)
                    continue

                current_car.set_status(1)

        self.print()

    def advance(self):
        # 前に車がいたら止まる、いなかったら進む単純ケース
        car_locations = [car.location for car in self.cars]
        for current_car in self.cars:
            if current_car.location == (self.length - 1):
                if 0 in car_locations:
                    continue

                current_car.location = 0

            else:
                # 前に車がいた場合は進めない
                if (current_car.location + 1) in car_locations:
                    continue

                current_car.location += 1

    def advance_slow_start(self):
        # 前に車がいたらとまる。走っているステータスの場合は、止まるへ変える
        # いなかったら、走っているステータスに変える
        # 前に車がいない かつ、走っているステータスの場合、前に進むというケース
        car_locations = [car.location for car in self.cars]
        for current_car in self.cars:
            if current_car.location == (self.length - 1):
                if 0 in car_locations:
                    current_car.set_status(0)
                    continue

                if current_car.status:
                    current_car.location = 0
                else:
                    current_car.set_status(1)

            else:
                # 前に車がいた場合は進めない
                if (current_car.location + 1) in car_locations:
                    # 車はとまる
                    current_car.set_status(0)
                    continue

                if current_car.status:
                    current_car.location += 1
                else:
                    current_car.set_status(1)

    def print(self):
        car_locations = [car.location for car in self.cars]
        for i in range(self.length):
            if i in car_locations:
                print("□", end="")
                continue
            print(" ", end="")
        print()

    def print_status(self):
        status_line = [""] * self.length
        for car in self.cars:
            status_line[car.location] = car.status
        print(status_line)

    def run_simple_start(self, steps):
        for var in range(steps):
            self.advance()
            self.print()

    def run_slow_start(self, steps):
        for var in range(steps):
            self.advance_slow_start()
            self.print()


class Car():
    def __init__(self):
        # 止まっている：0、走っている：1
        self.status = int()
        # 車列のどこにいるか
        self.location = int()

    def set_location(self, location):
        self.location = location

    def set_status(self, status):
        self.status = status
