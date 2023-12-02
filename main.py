# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


number = int(input("pls enter a number"))
sum=0
counter=0
while(number>0):
    counter+=1
    sum=sum+number
    if(number%2==1):
        print(number)
    for number in range(0, number+1, 1):
        print(number)
    for number in range(number, -1, -1):
        print(number)
    for num in range(1, number+1, 3):
        if(num%3==0):
            print(num)
    print(number)
    number=int(input("pls enter another number"))
    if (number<=0):
        break
print("the avg is=", sum/counter)

str = input("pls enter a word")
while(str != "stop"):
    print(str)
    str = input("pls enter a word")
    if("stop" in str):
        break

numbers=int(input("pls enter a number"))
newNum=1
for num in range(1, numbers+1, 1):
    newNum=newNum*num
    print(newNum)


sumHigh=0.0
countHigh=0.0
count=0.0

ask = float(input("pls enter the height"))
while(ask>0):
    if(ask>1.65):
        countHigh+=1
    count+=1
    sumHigh=sumHigh+ask
    ask = float(input("pls enter another height"))
print("the avg heigth is=", sumHigh/count)
print("num of ppl above 1.65 is=", countHigh)
