cnp = "1970525100134"
constanta = "279146358279"
s=0
for t in range(len(constanta)):
    s+=(int(cnp[t])*int(constanta[t]))
rez=s%11
if rez<10:
    c=rez
else:
    c=1
print(rez)
def cifre_an():
    ann = []
    for i in range(1,100):
        if i < 10:
            ann.append("0"+str(i))
        else:
            ann.append(str(i))
    return ann
def cifre_judet():
    judet = []
    for i in range(1,53):
        if i < 10:
            judet.append("0"+str(i))
        else:
            judet.append(str(i))
    return judet
def cifre_nastere():
    zi = []
    for i in range(1,32):
        if i < 10:
            zi.append("0"+str(i))
        else:
            zi.append(str(i))
    return zi
def cifre_luna():
    luna = []
    for i in range(1,13):
        if i < 10:
            luna.append("0"+str(i))
        else:
            luna.append(str(i))
    return luna
def cifre_nnn():
    nnn = []
    for j in range(1, 1000):
        if j < 10:
            nnn.append("0" + str(j))
        elif j >=10 and j <= 99:
            nnn.append("0"+str(j))
        else:
            nnn.append(str(j))
    return nnn
cod_judet = cifre_judet()
cod_nnn = cifre_nnn()
cod = [1,2,5,6,7,8]
zz = cifre_nastere()
an = cifre_an()
ll = cifre_luna()

smb_an = smb_zi = smb_nnn = smb_ll = smb_cod = c1 = c2 = smb_jdt = smb_c = 0
if cnp.isnumeric() == False:
    print("cnp invalid")
else:

    if len(cnp) == 13:
        str1=str2=""
        if int(cnp[0]) in cod:
            smb_cod = 1
        for a in range(1,13):
             if a<7:
                str1 += cnp[a]
             else:
                str2 += cnp[a]
        if str1[0:2] in an:
            smb_an = 1
        if str1[2:4] in ll:
            smb_ll = 1
        if str1[4:6] in zz:
            smb_zi = 1
            #print("cod str1 valid")
        if str2[0:2] in cod_judet:
            smb_jdt = 1
        if str2[2:5] in cod_nnn :
            smb_nnn = 1
        if c == int(str2[-1]):
            smb_c = 1
        if smb_jdt == 1 and smb_c == 1 and smb_nnn == 1 and smb_zi == 1 and smb_an == 1 and smb_an == 1 and smb_cod == 1:
            print("cnp valid")
        else:
            print("cnp invalid")

