# 給數字串列,將數字串列中的元素加總。
## 數字串列的初值、終值、遞增值
start = int(input('請輸入加總開始值?'))
end = int(input('請輸入加總終止值?'))
step = int(input('請輸入遞增減值?'))

## 用for迴圈做加總 + range()
sum = 0 #初始條件
for i in range(start, end, step): #判斷條件
    sum = sum + i #更新條件
    print('i為', i, '時,累加結果為', sum)


## 3. 中文串列的例子
sheet = ['牛奶', '蛋', '咖啡豆']
for i in range(0,len(sheet)): #位置索引從0開始[0,1,2]
    print (i, sheet[i]) #i是索引值,sheet[i]才是項目

## 4. 數字資料的例子
numbers = [123, 456, 789]
for i in numbers:
    print(i) #印拿出來的東⻄
numbers = [123, 456, 789]
for i in range(0, len(numbers)):
    print(i, numbers[i])# 索引和項目