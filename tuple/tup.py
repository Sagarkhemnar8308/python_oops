import sys
a=(1,2,3,4,5,6)
print(len(a))
print("size of a tuple is",sys.getsizeof(a),"bytes")

min_value = 0
max_value = 0

for i in a:
        if min_value is None or i < min_value:
            min_value = i
        if max_value is None or i > max_value:
            max_value = i

print("Minimum value in the tuple:", min_value)
print("Maximum value in the tuple:", max_value)
