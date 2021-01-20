#Simple python program to remove duplicates from a list

numbers = [5, 2, 23, 5, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
        
print(uniques)
