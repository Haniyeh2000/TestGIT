import math

# function prepare in python
def prime_factors(n):
    import primefac
    factor_n = list(primefac.primefac(n))
    print('p,q=',factor_n)
    return factor_n
# function gcd is: homon algoritm oghlidos
def gcd(n,e):
    y=[]
    u=[1,0]
    v=[0,1]
    g=[n,e]
    #one for az 0 to log(a)--->becuse daraghe algoritm az martabeh o(logn)
    for i in range(math.ceil(math.log(n,2))+2):
        if g[i+1]!=0:
            y.append(g[i] // g[i+1])
            g.append(g[i] % g[i+1])
            u.append(u[i] - y[len(y) - 1] * u[i+1])
            v.append(v[i] - y[len(y) - 1] * v[i+1])
        else:
            break
    print('g=', g)
    print('y=', y)
    print('v=', v)
    print('u=',u)
    #if yeki mandeh beh akhar g[]==1 bod yani ozveh makos hast
    if g[-2]==1 and g[-1]==0:
        if v[-2]<0:

            return v[-2]+g[0]
    else:
        return False

#block bandi function= text 6 caracter godah maconim and convert to int and return int number
def block(c,n):
    base=[]
    for j in range(0, len(c) - 5, 6):
        if int(c[j:j+6],16)<n:
            base.append(int(c[j:j + 6], 16))
        else:
            print('errrrrrrrrore pleas check size')
    return base

#pow function az daraghe sakhti o(logn)
def pow(power, base, n):
    result = 1
    for i in range(len(power)):
        # always mod in n because in system is n
        result = result * result % n
        if power[i] == '1':
            result = (result * base) % n
    return result

if __name__ == '__main__':
    chipper ='41A387CABD1C144C99E4B44CE2812A7696CE8A9B5941164741E91B82D89886700DD73A61C580BD75DFC0351D3D6BBF644408A77CB421A115C50'
    n = 16395979
    e = 4049
    print("RSA encrypted".center(4,'*'))
    factor_n = prime_factors(n)
    z_number = (factor_n[0]-1)*(factor_n[1]-1)
    print('z=',z_number)
    d=gcd(z_number,e)
    print('private key=',d)
    base= block(chipper,n)
    #for example 7^100= bin(100) is index and base is (7)
    power=bin(d)[2:]
    print("Decryption text...",end='')
    for i in range(len(base)):
        print(bytes.fromhex(str(hex(pow(power,base[i],n))[2:])).decode('utf-8'),end='') # convert int to char



