#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def angle_between_clock_hands(h, m, s):
    if not (0 < h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
        print("Ошибка: Некорректные значения времени.")
        return

    hour_angle = 0.5 * (60 * h + m)
    minute_angle = 6 * m
    angle = abs(hour_angle - minute_angle)

    if s != 0:
        second_angle = 0.1 * s
        angle = abs(angle - second_angle)

    return angle


h = int(input("Введите часы (от 1 до 23): "))
m = int(input("Введите минуты (от 0 до 59): "))
s = int(input("Введите секунды (от 0 до 59): "))

result = angle_between_clock_hands(h, m, s)

print(f"\nУгол между часовой стрелкой в начале суток и указанным моментом времени: {result} градусов.")
