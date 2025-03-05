##1
    #1 pwd
    #2 ls
    #3 git add homework.py --> git status --> git pull origin master
    #4 git add homework.py --> git push origin master
    #5 cd python_decal/olivia_decal/homework --> cat homework.py
    #6 vi <filename>
    #7 git add homework.py --> git commit -m "random message" --> git push origin master
    #8 The repository had some changes made to it and "Judy" did not pull the updates
        #Can do this: git pull origin master --> git add homework.py --> git commit -m "" --> git push origin master
    #9 If already in Users --> cd username/Recents

#2
#2.1
def checkDataType(input):
    return type(input)

print(checkDataType("probably not a float"))

#2.2
def evenOrOdd(int):
    if int % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(evenOrOdd(5))  ##Test Cases
print(evenOrOdd(210))

##3

def sumWithLoop(numbers):
    sum = 0
    for i in range(0, len(numbers)):
        sum += numbers[i]
    return sum

numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

##4

#4.1
def duplicateList(list):
    newList = []
    for i in range(0, len(list)):
        newList.append(list[i])
        newList.append(list[i])
    return newList

list = ['a','b','c','d']
print(duplicateList(list))

#4.2

#Original Code:
#def square(num) <== Missing a colon
    #return num * num

#Correct Code:
def square(num):
    return num * num

print(square(8))

##5