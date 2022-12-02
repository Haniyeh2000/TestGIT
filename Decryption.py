def out_of_range(array, index):

    if(index>=len(array)):
	
        return "00000000"
    else:
        return array[index]
		
		
		
def bitstring_to_byte(s):

    s=str(s)
	
    x=8 
	
    return [s[y-x:y] for y in range(x, len(s)+x,x)]
    
	
	
	
def binary_xor(data, key):

    l = len(key)
    return ''.join(
        str(int(data[i], 2) ^ int(key[i % l], 2)) for i in range(0,len(data))
    )
	
	
	
	
def gate(ascii):

    return ((ascii>=65 and ascii<=90) or (ascii>=97 and ascii<=122))
    

    
    
    
    
import numpy as np

key = []


def search_key(list,first,second):


    counter=0
    for i in range(0,len(list)):
        if(i >= len(key)):
            key.append(['-'])
        ascii = int(list[i],2)^32
        if(gate(ascii)):
            #print(i, chr(ascii), list[i], out_of_range(first,i), out_of_range(second,i))
            counter+=1
            if(gate(int(out_of_range(first,i),2)^ascii)):
                key[i].append(chr(int(out_of_range(first,i),2)^ascii))
            elif(gate(int(out_of_range(second,i),2)^ascii)):
                key[i].append(chr(int(out_of_range(second,i),2)^ascii))
    #print(counter)
    
    
def get_first(iterable, default=None):


    if iterable:
        for item in iterable:
            return item
    return default

    
def first_repeated(s):


     seen = set()
     for i, j in enumerate(s):
        if j in seen: # membership check in set is O(1)
            return j, s.count(j, i + 1) + 2 
        seen.add(j) 
        
def decode_binary_string(s):


    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))     

     
import os
os.system('cls')  # on windows

import glob
max_len=0
content=[]
for file in glob.glob("encryption\*.txt"):
    print(file)
    file = open(file, "r")
    file_read = file.read()
    print(file_read)
    #print(len(file_read))
    if(max_len<len(file_read)):
        max_len=len(file_read)
    content.append(format(int(file_read, 16), "0"+str(len(file_read)*4)+"b"))
    file.close()
    print(content)
'''   
print(max_len)
for i in range(0,len(content)):
    dif_len=(max_len*4)-len(content[i])
    dif_len=dif_len//8
    print(" ",dif_len)
    if(dif_len>0):
        content[i]=content[i]+("00000000"*dif_len)
    print(content[i])
    print(len(content[i]))
'''

for i in range(0,len(content)):
    for j in range(i,len(content)):
        if(i!=j):
            search_key( bitstring_to_byte(binary_xor(content[i], content[j])), bitstring_to_byte(content[i]),bitstring_to_byte(content[j]))
    
from collections import Counter 
print("\n\n\n key:")   
for i in range(0,len(key)):
    if(isinstance(key[i], list)):
        c= Counter(key[i])
        if(len(dict(c))>4):
            print(' ', end = '')
        else:    
            print(get_first(dict(c.most_common(1))), end = '')
    else:
        print(key[i], end = '')
        
        
        
        

print("")    
key_str = "It\u0092s your road and yours alone. Others may walk it with you, but no one can walk it for you. -R"
#print(len(key_str))
key_binarry = "".join(f"{ord(i):08b}" for i in key_str)


for i in range(0,len(content)):
    c=binary_xor(key_binarry, content[i])
    print(decode_binary_string(c))
    #print(len(decode_binary_string(c)))
