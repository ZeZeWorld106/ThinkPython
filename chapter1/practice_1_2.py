# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:01:30 2022

@author: Jarvis
"""

#在42分42秒中，一共有多少秒？
seconds = 42 * 60 + 42
print(f"42分42秒中，一共有：{seconds}s.")

#10千米相当于多少英里？
miles = 10 / 1.61
print(f"10千米相当于{miles}英里.")

#平均速度 & 平均速度是多少千米每小时
#1.平均速度
v_min = (seconds // 10)//60
v_sec = (seconds // 10)%60
print(f"跑一公里用了大约{v_min}m{v_sec}s。")
#2.平均速度是多少千米每小时
hour = seconds/3600
speed = 10 // hour
print(f"平均速度约：{speed}km/h")

