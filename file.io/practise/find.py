w="khemnar"

with open("ss.txt",'r') as f:
    data=f.read()
    
    if(data.find(w)!=-1):
        print('Found ',data.find(w) )
    else:
        print('Not Found')