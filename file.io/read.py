#mode of flies in python
# r, w , r+ , w+ , a, a+

f=open("open.txt","r")

# data=f.read()  # it has only the size 
line1=f.readline()
print( "seprae", line1)
# print(type(data))

f.close()



# 'r'  open for reading default
# 'w   open for writing truncationg the file first
# 'x' create a new file and open it for writing
# 'a' open for writing appending to the end of the file if it is exist
# 'b' binary mode
# 't' text mode (default)
# '+' open a disk file for updating reading and writing 