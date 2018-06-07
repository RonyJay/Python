# -*- coding: utf-8 -*-
import random
import csv
#生成一个code
def getcode():
    s='0123456789ZXCVBNMASDFGHJKLQWERTYUIOP'
    code=[]
    for i in range(0,4):
        reg=[]
        for j in range(0,4):
            reg.append(s[random.randint(0,len(s)-1)])
        code.append(''.join(reg))
    couponList=[]
    couponList.append('-'.join(code))
    return couponList

#写入list
coupon_list=[]
for i in range(10000):
    coupon_list.append(getcode())



with open('test.csv','w',newline='') as couponList:
    csv_write=csv.writer(couponList)
    for data in coupon_list:
        csv_write.writerow(data)


