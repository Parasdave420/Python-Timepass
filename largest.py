#A simple python program to find the largest number from a given list

numbers = [3, 8 , 15,  120, 9]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
