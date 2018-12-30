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


def test_car_class():
    car = car_class.Car()
    LOCATION = 10
    car.set_location(LOCATION)
    assert car.location == LOCATION

    STATUS = 1
    car.set_status(STATUS)
    assert car.status == STATUS
