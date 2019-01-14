#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cellautomata import car_class

if __name__ == '__main__':
    CAR_LENGTH = 20  # 車列の長さ
    CAR_NUM = 10  # 車の台数
    STEPS = 100  # ステップ数

    # 初期車列の生成
    # car_line = car_class.CarLine(CAR_LENGTH, CAR_NUM)
    # car_line.print()

    # car_line.run_simple_start(STEPS)

    # シンプルモデルの車両の密度と流量の関係のグラフを表示
    car_class.show_scatter_plot_slow_start(CAR_LENGTH)
