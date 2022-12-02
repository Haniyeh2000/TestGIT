# def xor(p,size):
#     tex_xor = ''
#     text=p[0]
#     key=p[1]
#     for i in range(size):
#         # If the Character matches
#         for j in range(8):
#             if (text[i][j] == key[i][j]):
#                 tex_xor += "0"
#         else:
#             tex_xor += "1"
#     return tex_xor

def creat_key(c11,c11_bi,ind):
    c11_xor=''
    c11_xor_primery=[]
    key_int = []
    for k in range(len(c11)):
        # If the Character matches
        for y in range(8):

            if (c11_bi[k][y] == c11[k][y]):
                c11_xor += "0"
            else:
                c11_xor += "1"
        c11_xor_primery.append(c11_xor)
        c11_xor=''
    asci_c11=[]

    for j in range(0, len(c11_xor_primery)):
        an_integer = int(c11_xor_primery[j], 2)
        asci_c11.append(chr(an_integer))
    print('p=',ind,''.join(asci_c11))
    return c11_xor_primery
if __name__ == '__main__':

    c = [0]*11
    c[0]="1D1CF7534D161C015243171D1505490F4E1341004F011D5353140F0C0B004A00260748041E0441141259541841181959491E55041D54074E1C4F18435207550049030A0E4F4331480C0C0F535720424B650D1D530901"
    c[1]="101BE701000D061817001B1C4108490C0710451D4355011C00050301FC110E572E071C00521A544D0D10561E0F0B4B530619451807114845151C10BE5342191D460B4100424E365406170B003D0E0E18"
    c[2]="1E1CF707481C1D550B4F074F150C490F054459161A5511124E41031D4E1C41556F00000C1C1800140E0C00140002F954455459181CE61A45591D1C4B48165B540D4E2745011C1C00250E1C44"
    c[3]="1E1BE018001E0603175352160E11000C0B054E10011252124E054C1F1B175E4F3C1148041C170001081F4557081F4B450404540E4903015411000058000B015AB44EF9004F3D114513090B4E57290D1C4B001A47"
    c[4]="1918F31D53590E0717001C00150C490F095F000903141C1D490F0B4F07160E4539111A1C061B4903065700E1414C2F5700134803493046003C0606494E0A1A03451C"
    c[5]="061AFE0A00091A01524F140941114E150708000D00181D01520E1B4F190D4F546F0D071052125208410E491B0D05054749004F570D1D0D00110E03454E05551845081B001A00014F0D044000E1414C3B410B184F463F1B43181C0641"
    c[6]="0000B21A53590B0000491C08410B55134E00410B04100107000C03020B0B5A536F0000040653570841145504154C0D4F0A0153571D1B48531C0A55584807551849090754414EF30043201C490415031F4C0C546F080E0153101C"
    c[7]="0000B21A535901100445004F150B4F410205541C4F011D5342044C1806045A00361B1D451F1A47051559481617094B420C114E594954FE003E0A1A5E470755314C070054"
    c[8]="0D1BFCE1545918141B5452090E1600150601000B06121A07000E1C1F01175A55211D1C1C5C53631F0418541241051F0E4954B6572E1107521E0A556E45101B15520A4F73070F12"
    c[9]="1A01F110450A1C551B53520E41084F141D1D000D0A14111B4513424F27110E532A101D061700001E0C185203411C0E4F19184557001A1C4F591B1D454E091C1A474E1B480A174543020FFC54570D03184547540D462D1B4C154F324F544821"
    c[10]="061AF7534F1F4F341E42171D154465080017541C061B5500000C031C1A454841221B1D1652025502151C5357081F47004B334F13491007450A4F1B435442051841174F44060D000014081A485715040E001C1A49100A00531C4105"


    #seprate tow caracters and conversion binary
    size_max_c = len(max(c, key=len)) // 2
    arr_binary = ['0'] * 11
    arr = ['00000000'] * size_max_c
    index = 0
    for i in range(11):
        for j in range(0,len(c[i]), 2):
            # if i==1 and index==1:
            #     print('arr[1][0]=',bin(int(c[i][j] + c[i][j + 1], base=16)),'  ',c[i][j] , c[i][j + 1])
            temp2 = bin(int(c[i][j] + c[i][j + 1], base=16))
            arr[index] = temp2[2:].zfill(8)
            index += 1
        index = 0
        arr_binary[i] = arr
        #c1_binery=['0101010'],['01010101'],......
        #c10_binery=['00001010']
        arr = ['00000000'] * size_max_c


    #xor c1, c2, ......,C10 with c11
    text_xor=[]
    andis_xor=[]
    x=[]


    for i in range(11):
        for j in range(i,11):
            if i!=j:
                tex_xor = ''
                text = arr_binary[i]
                key = arr_binary[j]
                for k in range(size_max_c):
                    # If the Character matches
                    for y in range(8):

                        if (text[k][y] == key[k][y]):
                            tex_xor += "0"
                        else:
                            tex_xor += "1"
                andis=[i,j]
                text_xor.append(tex_xor)
                andis_xor.append(andis)

    print(c[10])

    c_xor_sort=[]
    for j in range(11):
        for i in range(len(text_xor)):
            if j in andis_xor[i]:
                c_xor_sort.append(text_xor[i])

    # seperete 8 bit 8bit for convert ASCI
    size_xor_arr=len(c_xor_sort[0])
    size_char_arr=size_xor_arr//8
    number=0
    asci_c =[]
    asci_c_primary=[]
    for i in range(len(c_xor_sort)):
        for j in range(0,size_xor_arr,8):
            an_integer = int(c_xor_sort[i][j:j+8],2)
            if (an_integer >= 65 and an_integer <= 90) or (an_integer >= 97 and an_integer <= 122):
                asci_c.append(chr(an_integer))
            else:
                asci_c.append('0')
        asci_c_primary.append(asci_c)
        asci_c = []


    # for i in range(len(asci_c_primary)):
    #     print(" ")
    #     for j in range(len(asci_c_primary[i])):
    #         print(asci_c_primary[i][j],end=' ')
    # print('\n')

    i=100
    for i in range(100,109):
        print('c=',asci_c_primary[i])

    c11="The of Albert Einstein's most famous quotes is, "+'"God does not play dice with the univers."'
    y = ' '.join(format(ord(x), 'b').zfill(8) for x in c11).split()
    print('bynery p11', y)
    x=arr_binary[10]
    print('baynery xor for key',x)
    print('After guessing the sentence:', c11)
    ky_int=creat_key(y,x,20)
    print(ky_int)
    for i in range(10):
        x=arr_binary[i]
        kyy=creat_key(ky_int,x,i)

    print(arr_binary[1])
