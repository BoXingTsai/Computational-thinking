#習題一
print("上衣一件300元,褲子一件350元,背心一件400元")
a=int(input("上衣買的數量:"))
b=int(input("褲子買的數量:"))
c=int(input("背心買的數量:"))
s=a*300+b*350+c*400
print("總價:%d" %(s))

#習題二
print("一罐20元一打200元,不滿一打個別賣")
a=int(input("購買的數量:"))
if(a<12):
    s=a*20
else:
    x=a%12
    y=(a-x)/12
    s=x*20+y*200
print("總數量:%d" %(a),"總價:%d" %(s))
#習題三
a=float(input("第一次期中考成績:"))
b=float(input("第二次期中考成績:"))
c=float(input("期末考成績:"))
s=a+b+c
z=(a+b+c)/3
print("總分:%d" %(s), "平均:%f" %(z))