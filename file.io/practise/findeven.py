# def even_in_file():
#     with open("ss.txt","r") as f:
#         data=f.read()
#         num=""
#         for i in range(0,len(data)):
#             if(data[i] == ","):
#                 print(int(num))
#                 num=""
#             else:
#                 num+=data[i]
#         if(int(num) % 2 == 0):
#             print(num)
# even_in_file()


count=0
with open("ss.txt","r") as f:
    data=f.read()
    sp=data.split(",")
    for even in sp:
        if(int(even)%2==0):
            count=count+1
            print(even)
print(count)