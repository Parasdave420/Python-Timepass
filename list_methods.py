#program to demonstrate methods available for list in python


numbers = [5, 2, 5, 1, 6]

#add number at the end of list
numbers.append(25)
print(numbers)

#insert item on specific index list.insert(index, item)
numbers.insert(2, 22)
print(numbers)

#remove specific item from a list
numbers.remove(2)
print(numbers)

#remove last item from list
numbers.pop()
print(numbers)

#print specific item's index (first appearance)
print(numbers.index(1))

#check item in list 
print(50 in numbers)

#count number of appearance of an item
print(numbers.count(5))

#sort method for list
numbers.sort()
print(numbers)

#reverse the list 
numbers.reverse()
print(numbers)

#copy the list
numbers2 = numbers.copy()
numbers.apend(10)
print(numbers)
print(numbers2)

#clear whole list
numbers.clear
print(numbers)
