def pow(power, base, p):
    result = 1
    x=12
    for i in range(len(power)):
        # always mod in n because in system is n
        result = result * result % p
        if power[i] == '1':
            result = (result * base) % p
        print(result)
    return result


print(pow(bin(13)[2:],5,23))
print("hi github how are you???")