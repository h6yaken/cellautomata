#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cellautomata import car_class

if __name__ == '__main__':
    CAR_LENGTH = 20  # 車列の長さ
    CAR_NUM = 10  # 車の台数

    car_line = car_class.CarLine(CAR_LENGTH, CAR_NUM)
    # 初期車列の表示
    car_line.print()

    for var in range(20):
        # スロースタートルールを適用したモデルの車列を表示
        car_line.advance_slow_start()
        car_line.print()
