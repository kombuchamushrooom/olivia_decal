#HOMEWORK 3
#1
def computePower(x, y):
    i = 1
    result = 0
    while i < y:
        result += x * x
        i += 1
    print(result)

x=3
y=2

computePower(x, y)

#2
readings = [15, 14, 17, 23, 28, 20]

def temperatureRange(readings):
    x = max(readings)
    y = min(readings)
    new_tuple = (y, x)
    print(new_tuple)
 
temperatureRange(readings)

#3
def isWeekend(day):
    if (day == 6) or (day == 7):
        return 1 > 0 
    else:
        return 0 > 1
print(isWeekend(7))

#4
def fuel_efficiency(distance, fuel):
    return distance/fuel
    print(fuel_efficiency(20, 3))

# #5
def decodeNumbers(num): ##Valid only for integers not ending in 0
    digits = num // 10
    last_digit = num % 10
    magnitude = len(str(digits))
    if last_digit == 0:
        return str(last_digit) + str(digits)
    else:
        return digits + (last_digit * pow(10, magnitude))
num = 16792390 
print(decodeNumbers(num))


#6
#6.1
numbers = [2024, 98, 131, 2, 3, 73]
def find_min_with_while_loop(nums):
    min = nums[0]
    i = 1
    while i < len(nums):
        if (nums[i] < min):
            min = nums[i]
        i += 1
    return min
print(find_min_with_while_loop(numbers))

#6.2
def find_max_with_while_loop(nums):
    max = nums[0]
    i = 1
    while i < len(nums):
        if (nums[i] > max):
            max = nums[i]
        i += 1
    return max
print(find_max_with_while_loop(numbers))


#7
def vowel_and_consonant_count(text):
    vowels = 0
    consonants = 0
    i = 0
    while i < len(text):
        if (text[i] == 'a') or (text[i] == 'i') or (text[i] == 'e') or (text[i] == 'o') or (text[i] == 'u') or (text[i] == 'A') or (text[i] == 'E') or (text[i] == 'I') or (text[i] == 'O') or (text[i] == 'U'):
            vowels += 1
            i += 1
        elif (text[i].isalpha() == False):
            i += 1
        else:
            consonants += 1
            i += 1
    new_tuple = (vowels, consonants)
    return new_tuple

text = "UC Berkeley, founded in 1868!" ##Test case has 8 vowels, not 4
print(vowel_and_consonant_count(text))

#8
def digital_root(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    return sum
num1 = 2468 ##should throw 20
print(digital_root(num1))
