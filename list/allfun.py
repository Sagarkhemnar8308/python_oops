numbers = [45, 67, 89, 34, 12, 56, 37, 3, 3, 3, 3, 42]

# numbers.append(143)  #it can add the element in the last
# numbers.sort()  #it get a sorting
# numbers.reverse() #it get reverse a list
# numbers.insert(2,45) ## we pass a position and number to pass that to that position
# numbers.remove(45)# we can pass a value and that will be remove from the list
# numbers.pop(2)  # we can pass a index or it automatic remove the -1
# numbers.clear() # it will clear a list
a = numbers.copy()
b = numbers.count(3)  # it check a  3 in list that how many times 3 is occur in the list
c = numbers.index(67)  # it check a index of a count
numbers.extend([12,34,55])## it will add that mis it get a  concat
print(a, b, c, numbers)
