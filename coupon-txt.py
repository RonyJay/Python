import random
def getcode():
    s='0123456789ZXCVBNMASDFGHJKLQWERTYUIOP'
    code=[]
    for i in range(0,4):
        reg=[]
        for j in range(0,4):
            reg.append(s[random.randint(0,len(s)-1)])
        code.append(''.join(reg))
    return '-'.join(code)


#生成couponlist列表
couponList=[]
for i in range(20):
	couponList.append(getcode())



# with open('test.csv','w',newline='') as couponList:
#     csv_write=csv.writer(couponList)
#     for data in coupon_list:
#         csv_write.writerow(data)

fileObj=open('coupon.txt','w')
for data in couponList:
	fileObj.write(data)
	fileObj.write('\n')
fileObj.close()