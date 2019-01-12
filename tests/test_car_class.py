#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cellautomata import car_class


def test_car_line_class():
    CAR_LINE_LENGTH = 20
    CAR_NUM = 10
    car_line = car_class.CarLine(CAR_LINE_LENGTH, CAR_NUM)
    assert car_line.length == CAR_LINE_LENGTH
    assert car_line.num == CAR_NUM
    assert len(car_line.cars) == CAR_NUM
    for car in car_line.cars:
        assert 0 <= car.location <= CAR_LINE_LENGTH - 1

    # advanceのテスト
    CAR_NUM = 2
    car_line = car_class.CarLine(CAR_LINE_LENGTH, CAR_NUM)
    assert len(car_line.cars) == CAR_NUM
    car_line.cars[0].location = 1
    car_line.cars[1].location = 2
    car_line.advance()
    assert car_line.cars[0].location == 1
    assert car_line.cars[1].location == 3

    car_line.cars[0].location = 1
    car_line.cars[1].location = 3
    car_line.advance()
    assert car_line.cars[0].location == 2
    assert car_line.cars[1].location == 4

    car_line.cars[0].location = 0
    car_line.cars[1].location = 19
    car_line.advance()
    assert car_line.cars[0].location == 1
    assert car_line.cars[1].location == 19

    car_line.cars[0].location = 10
    car_line.cars[1].location = 19
    car_line.advance()
    assert car_line.cars[0].location == 11
    assert car_line.cars[1].location == 0

    # advance_slow_startのテスト
    CAR_NUM = 2
    car_line = car_class.CarLine(CAR_LINE_LENGTH, CAR_NUM)
    assert len(car_line.cars) == CAR_NUM
    # 前に車がいない/走っているステータスの場合、前に進む
    car_line.cars[0].location = 1
    car_line.cars[0].status = 0
    car_line.cars[1].location = 2
    car_line.cars[1].status = 1
    car_line.advance_slow_start()
    assert car_line.cars[0].location == 1
    assert car_line.cars[0].status == 0
    assert car_line.cars[1].location == 3
    assert car_line.cars[1].status == 1

    # 前に車がいない/止まっているステータスの場合、ステータスを走っている状態へ変える
    car_line.cars[0].location = 1
    car_line.cars[0].status = 0
    car_line.cars[1].location = 2
    car_line.cars[1].status = 0
    car_line.advance_slow_start()
    assert car_line.cars[0].location == 1
    assert car_line.cars[0].status == 0
    assert car_line.cars[1].location == 2
    assert car_line.cars[1].status == 1

    # 前に車いる/走っているステータスの場合、止まっている状態へ変える
    car_line.cars[0].location = 1
    car_line.cars[0].status = 1
    car_line.cars[1].location = 2
    car_line.cars[1].status = 0
    car_line.advance_slow_start()
    assert car_line.cars[0].location == 1
    assert car_line.cars[0].status == 0
    assert car_line.cars[1].location == 2
    assert car_line.cars[1].status == 1

    # 前に車がいる/止まっているステータスの場合、位置も状態も変わらない
    car_line.cars[0].location = 1
    car_line.cars[0].status = 0
    car_line.cars[1].location = 2
    car_line.cars[1].status = 0
    car_line.advance_slow_start()
    assert car_line.cars[0].location == 1
    assert car_line.cars[0].status == 0
    assert car_line.cars[1].location == 2
    assert car_line.cars[1].status == 1

    # 最後尾の考慮が正しいか
    car_line.cars[0].location = 0
    car_line.cars[0].status = 0
    car_line.cars[1].location = 19
    car_line.cars[1].status = 0
    car_line.advance_slow_start()
    assert car_line.cars[0].location == 0
    assert car_line.cars[0].status == 1
    assert car_line.cars[1].location == 19
    assert car_line.cars[1].status == 0

    car_line.cars[0].location = 1
    car_line.cars[0].status = 0
    car_line.cars[1].location = 19
    car_line.cars[1].status = 1
    car_line.advance_slow_start()
    assert car_line.cars[0].location == 1
    assert car_line.cars[0].status == 1
    assert car_line.cars[1].location == 0
    assert car_line.cars[1].status == 1

    car_line.cars[0].location = 1
    car_line.cars[0].status = 0
    car_line.cars[1].location = 19
    car_line.cars[1].status = 0
    car_line.advance_slow_start()
    assert car_line.cars[0].location == 1
    assert car_line.cars[0].status == 1
    assert car_line.cars[1].location == 19
    assert car_line.cars[1].status == 1


def test_car_class():
    car = car_class.Car()
    LOCATION = 10
    car.set_location(LOCATION)
    assert car.location == LOCATION

    STATUS = 1
    car.set_status(STATUS)
    assert car.status == STATUS
