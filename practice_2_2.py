# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:11:16 2022

@author: Jarvis
"""

#求解半径为5的球体体积
pi = 3.141592653589793
r = 5

v = 4/3 * pi * r**3

print(f"半径为5的球体体积为：{v}")

#求解买60本书要花多少钱
price = 24.95
sale = price * 0.6
number = 60
book_fee = number * sale
trans_fee = 3 + (number - 1) * 0.75
total_fee = trans_fee + book_fee

print(f"买书一共花了{trans_fee}美元。")

#回家吃饭几点
left_home = "6:53 a.m."

#计算总共用时
start = 6*60 + 53
fm = 8*60+15
rm = (7*60+12)*3
total = start + fm + rm

#进行单位换算
total_h = int(total/3600)
total_min = int((total%3600)/60)
total_sec = int((total%3600)%60)
print("跑步用时：{}:{}:{}.".format(total_h,total_min,total_sec))

#做格式调整
if total_sec + 0 >= 60:
    total_sec = total_sec + 0 - 60
    total_min += 1
else:
    total_sec = total_sec + 0
    
if total_min + 53 >= 60:
    total_min= total_min + 53 - 60
    total_h += 1
else:
    total_min = total_min + 53

if total_h + 6 >= 24:
    total_h = total_h + 6 - 24
else:
    total_h = total_h +6

print("到家时间：{}:{}:{}".format(total_h, total_min, total_sec))


