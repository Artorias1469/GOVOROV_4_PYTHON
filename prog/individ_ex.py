#!/usr/bin/env python3
# -*- coding: utf-8 -*-

length = float(input("Введите длину параллелепипеда: "))
width = float(input("Введите ширину параллелепипеда: "))
height = float(input("Введите высоту параллелепипеда: "))

volume = length * width * height
surface_area = 2 * (length * width + width * height + height * length)

print("\nОбъем параллелепипеда:", volume)
print("Площадь боковой поверхности параллелепипеда:", surface_area)
