numberList=[1,2,3,4,5,6,7,8,9,10]
max = numberList[0]
for num in numberList:
    if max < num:
        max = num
        print(max)