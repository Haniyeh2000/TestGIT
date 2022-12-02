def bynery(text):
    size_byner = len(text) // 2
    arr_b = ''
    for i in range(0, len(text), 2):
        t = bin(int(text[i] + text[i + 1], base=16))
        arr_b += (t[2:].zfill(8))
    return arr_b


def creat_key(digit):
    import random
    set = '0123456789ABCDEF'
    key = ''
    for i in range(digit):
        key += random.choice(set)
    return key

def xor(text,key):
    tex_xor = ''
    for i in range(len(text)):
        if (text[i] == key[i]):
            tex_xor += "0"
        else:
            tex_xor += "1"
    return tex_xor



c = "5410CC"
p = "010199"
Bynery_c=bynery(c)
Bynery_p=bynery(p)
print('bp=',Bynery_p,'bc=',Bynery_c)
flag=True
index=0
while flag:
    k1 = creat_key(6)
    k2 = creat_key(6)
    Bynery_k1=bynery(k1)
    Bynery_k2=bynery(k2)
    # print('bk1=',Bynery_k1,'bk2=',Bynery_k2)
    xor1=xor(Bynery_p,Bynery_k1)
    xor2=xor(Bynery_c,Bynery_k2)
    index=index+1
    if xor1==xor2:
        flag=False
        print("hora")
        print("index find key=",index,'  xor p , k1', xor1,'  xor c , k2', xor2)
        print('k1=', k1, 'k2=', k2)
        break

