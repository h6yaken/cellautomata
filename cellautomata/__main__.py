#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cellautomata import car_class

if __name__ == '__main__':
    CAR_LENGTH = 50  # 車列の長さ
    CAR_NUM = 30  # 車の台数

    # 初期車列の生成
    car_line = car_class.CarLine(CAR_LENGTH, CAR_NUM)

    STEPS = 20
    car_line.run_simple_start(STEPS)
