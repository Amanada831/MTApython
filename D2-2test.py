# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:22:23 2021

@author: TQC
"""
score = []
while True:#一直進入迴圈模式
    inscore = int(input("分數"))
    if inscore=="":
        break#直到碰到break才會跳出迴圈
    else:
        score.append(inscore)
        score2 = sorted(score,reverse=True) 
#        scort.sort()
#        scort.reverse()  #由小到大排列
    print(score2)       