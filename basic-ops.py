#Inserting Elements
numbers = [10, 20, 30]

numbers.append(40)

print(numbers) 

numbers.insert(1, 15)

print(numbers) 

#Deleting Elements
numbers.remove(20)

print(numbers)

# To remove an element by its index, use pop()
numbers.pop(2)

print(numbers) 

#Searching for an Element

print(15 in numbers)

#Find the index of an element using index():

print(numbers.index(15))

#Traversing a List

for num in numbers:

    print(num)

#Sorting a List
numbers.sort()

print(numbers) 

#Reversing a List
numbers.reverse()

print(numbers)

# List Comprehensions
squares = [x**2 for x in range(1, 6)]

print(squares)