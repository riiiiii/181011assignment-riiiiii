# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:51:59 2018

@author: Risa Mukai
"""

#paiza8-05-2

#coding: utf-8
#学生メソッドを作る

class Gakusei:
    def __init__(self,kokugo,sansu):
        self.kokugo=kokugo
        self.sansu=sansu
    def sum(self):
        return int (self.kokugo+self.sansu)
yamada=Gakusei(70,43)
print("合計は"+str(yamada.sum())+"点です")
        