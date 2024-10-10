def find_line_num():
    line_no=1
    data=True
    word="sdfdgfg"
    with open("ss.txt",'r') as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
            line_no+=1
    return -1

find_line_num()