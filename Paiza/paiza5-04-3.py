# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:03:58 2018

@author: Risa Mukai
"""

#5-04-3
#ループで合計を計算しよう

points={"国語":70,"算数":35,"英語":52}
sum=0
for key in points:
    sum+=points[key]
print(int(sum))