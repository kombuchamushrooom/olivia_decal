##Homework 4

#1

#2
#2.1
randomList = []

for i in range(0, 21, 1):
    randomList.append(i)
print(randomList)

#2.2
def squareList(list):
    newList = []
    for i in range(0,len(list)):
        newList.append(pow(list[i], 2))    
    return newList

another_random_list =squareList(randomList)
print(another_random_list)

#2.3
def first_fifteen_elements(list):
    return list[0: 15]
print(first_fifteen_elements(another_random_list))

#2.4
def every_fifth_element(list):
    fifth_list = []
    for i in range(4, len(list), 5):
        fifth_list.append(list[i])
    return fifth_list
print(every_fifth_element(another_random_list))

#2.5
def evil_function(list):
    evil_list = []
    for i in range(len(list) - 1, 0, -3):
        evil_list.append(list[i])
    return evil_list
print(evil_function(another_random_list))

#3
#3.1
rows = 5
cols = 5
matrix = [] * rows
for i in range(0, rows, 1):
    rownum = []
    for j in range(1, cols + 1, 1):
        rownum.append(j + i * 5)
    matrix.append(rownum)
print(matrix)

#3.2
def modified_2d_list(matrix):
    newmat = matrix
    for i in range(0, rows, 1):
        rownum = []
        for j in range(1, cols + 1, 1):
            if (j + i*5) % 3 == 0:
                rownum.append('?')
            else:
                rownum.append(j + i * 5)
        newmat.append(rownum)
    return newmat
print(modified_2d_list(matrix))

#3.3
a = modified_2d_list(matrix)
def sum_non_question_elements(list):
    sum = 0
    for i in range(0, len(list[0]), 1):
        for j in range(0, len(list[i]), 1):
            if list[i][j] != '?':
                sum += list[i][j]
    return sum
print(sum_non_question_elements(a))