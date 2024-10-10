with open("ss.txt",'r') as f:
    data= f.read()
    new=data.replace("sagar","dhanesh")
    
    print(new)