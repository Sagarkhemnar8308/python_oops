# Python program to interchange first and last elements in a list
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# l1[0] = 12
# l1[-1] = 12
# print(l1)

# list addition
# l2 = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
# sum = 0
# for i in range(len(l2)):
#     sum += l2[i]
#    # print(sum, i, l2)
# print("Total sum of a l2 list is " + str(sum))

# Python program to swap two elements in a list
# l3 = [12, 34, 22, 65, 78, 99]

# def swap(list, pos1, pos2):
#    list[pos1], list[pos2] = list[pos2], list[pos1]
#    return list

# a = swap(l3, 0, -1)
# print(a)

# Python – Swap elements in String list
# strrr = ["sagar", "samir", "rohit"]

# def swap_str(list, pos1, pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list

# s = swap_str(strrr, 0, -1)
# print(s)

# Maximum of two numbers in Python
# def max(a, b):
#     if(a > b):
#         print(str(a) + " is greater than", str(b))
#     else:
#         print(str(b) + " is greater than", str(a))

# m1 = max(23, 34) 

# Minimum of two numbers in Python
# a = 342
# b = 343

# if(a < b):
#     print(a, "is minimum than ", b)
# else:
#     print(b, "is minimum than ", a)
    
# Python | Ways to check if element exists in list

# list1=[12,24,36,48,60,72,84,96,108,120]

# a=int(input("enter a number exist in list"))

# if a in list1:
#     print("Exist")
# else:
#     print("Not Exist")

# Different ways to clear a list in Python
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b=a.clear()
# a=[]
# print("a list is ", a)

# Python | Reversing a List
# reversea = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# reversea.reverse()
# print(reversea[3:-1])

# Python | Count occurrences of an element in a list
# def find_count(list, county):
#     new_count = list.count(county)
#     return new_count

# arr = [1, 2, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6]
# find = find_count(arr, 3)
# print("find count is ", find)

# Python Program to find sum and average of List in Python
# def sum_avg(list):
#     sum = 0
#     for i in range(len(list)):
#         sum += list[i]
#     return (sum / len(list))

# list1 = [96,97, 98]
# avg = sum_avg(list1)
# print("average is a ", avg)

# Python | Sum of number digits in List

# list11 = [122, 133, 144, 155, 166, 177, 188, 199, 200]

# res = []
# for i in list11:
#     sum = 0
#     for c in str(i):
#         sum += int(c)
        
#     res.append(sum)
    
# print("response ke", res) 

# Python | Multiply all numbers in the list

# list11 = [1, 2, 3, 4]

# mul = 1
# for i in list11:
#     print(i)
#     mul *= i
# print(mul)

# Python program to find smallest number in a list
# list1=[12,34,5,652,354,342,3,13]

# list1.sort()

# print(list1[0])
# print(list1[-1])

# Python program to find a even number in the list

# list2=[1,22,3,43,5,6,7,8,9,0]
# even_list=[]

# for i in list2:
#     if i % 2 != 0:
#         even_list.append(i)
        
# print(even_list)
        
# Python program to count Even and Odd numbers in a List

# list3=[34,45,56,7,89,23,12,99]
# evencount=0
# oddcount=0

# for i in list3:
#     if(i % 2 == 0):
#         evencount+=1
#     else:
#         oddcount+=1
    
# print(evencount, oddcount)

# Python program to print positive numbers in a list
# list1 = [12, -7, 5, 64, -14]

# for i in list1:
#     if(i > 0):
#         print(i, end=" ")

# list Program to print duplicates from a list of integers


def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k,_size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated    
            
 
# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print (Repeat(list1))
