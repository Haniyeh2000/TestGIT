
def dlog(g,p,pub_key) :
    pri_key = 0
    for i in range(1,p):
        number=pow(bin(i)[2:], g, p) % p
        print('i=',i,number)
        if number == pub_key:
            pri_key = i
            break

    if pri_key == 0:
        print("NOT FOUND PRIVATE KEY...IM SORRY")
    else:
        return pri_key

def pow(power, base, p):
    result = 1
    for i in range(len(power)):
        # always mod in n because in system is n
        result = result * result % p
        if power[i] == '1':
            result = (result * base) % p
    return result


def block(c, p):
    Int_c = []
    for j in range(0, len(c) - 5, 6):
        if int(c[j:j+6],16)<p:
            Int_c.append(int(c[j:j + 6], 16))
        else:
            print('errrrrrrrrore pleas check size')
    return Int_c

if __name__ == '__main__':
    c1 ='5'
    c2 ='2'
    pub_key = 10
    g = 19
    p = 23
    a = 5861237

    Int_c1=block(c1,p)
    Int_c2=block(c2,p)
    # print(Int_c1)
    # print(Int_c2)
    pri_key=dlog(g, p, pub_key)
    print('p',pri_key)
    pow_num = p - 1 - pri_key
    for i in range(len(Int_c1)):
        print(bytes.fromhex(str(hex(pow(bin(pow_num)[2:], Int_c1[i], p)*Int_c2[i]%p)[2:])).decode('utf-8'), end='')

