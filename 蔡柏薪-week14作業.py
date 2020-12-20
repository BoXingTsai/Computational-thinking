names = ["蔡柏薪", "陳妤瑄", "甘庭銨", "林昱承","游佳樺","簡郁虹"]
dessert = ["抹茶", "巧克力", "蛋捲", "千層派", "甜甜圈", "蛋塔"]
for i in range(len(names)):
    print("Hi,my name is",names[i],".My favorite dessert is",dessert[i])
    
a=int(input('請輸入開始值:'))
n=int(input('請輸入終止值:'))
s=int(input("請輸入遞增值:"))
sum=0
for n in range(a,n+1,s):
    sum=sum+n**2
    print('n為', n, '時，累加結果為', sum)
