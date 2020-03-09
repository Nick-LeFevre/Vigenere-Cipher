def main():
    pn = ["1","3","5","7","9","11","15","17","19","21","23","25"]
    lo = "!"
    alpha = []
    rt = 0 #value for rotating englihs frequency
    for i in range(26):
        alpha.append(chr(97+i))
    input1 = input("Enter ciphertext: ")
    f,e = freq(input1.lower(),alpha,pn,rt) #getting lists of frequent ciphertext and english text
    for o in range(26): #loop that tries every possible combination
        for i in range(len(f)):
            for j in range(len(f) -1):
                for x in range(len(e)):
                    for z in range(len(e) - 1):
                        lo = pt_attack(f[i],f[j],e[x],e[j],alpha,pn,input1.lower(),lo)
        rt += 1
        f,e = freq(input1.lower(),alpha,pn,rt)

def posletter(alpha,fl,rt):
    eng = [7,1,3,4,13,3,2,3,8,0,0,4,3,8,7,3,0,8,6,9,3,1,1,0,1,0] #most frequent letter occurences in the english alphabet
    eng2 = list(eng)
    alpha2 = list(alpha)
    temp = []
    eng.sort(reverse = True)
    alpha2.sort(reverse = True)
    r_eng = rotate(eng,rt)
    alpha2 = rotate(alpha,rt)
    for i in range(6):
        l = alpha[eng2.index(r_eng[i])]
        if l not in temp:
            temp.append(l)
        else:
            temp.append(alpha2[i])
    return temp

def freq(ct,alpha,pn,rt):
    freq = [0]*26
    h = []
    fl = []
    for i in ct:
        if i != " ":
            freq[ord(i)-97] += 1
        h = list(freq)
        h.sort(reverse = True)
        alpha2 = list(alpha)
        alpha2.sort(reverse = True)
        for i in range(6):
            temp = alpha[freq.index(h[i])]
            if temp not in fl:
                fl.append(temp)
            else:
                fl.append(alpha2[i])
        posletters = posletter(alpha,fl,rt)
        return fl,posletters

def pt_attack(c1,c2,p1,p2,alpha,pn,ct,lastout): #uses the equations and plugs the numbers in to find keys A and B
    c1 = ord(c1)-97
    c2 = ord(c2)-97
    p1 = ord(p1)-97
    p2 = ord(p2)-97
    d = (p1-p2)%26
    if str(d) in pn:
        d = mi(d)
        a = (d*(c1-c2))%26
        b = (d*(p1*c2+p2*c1))%26
        if str(a) in pn:
            out = decrypt(a,b,ct,alpha)
            if out != lastout:
                print(out + " A:" + str(a) + " B:" + str(b))
            lastout = out
            return lastout

def rotate(l,n):
    return l[n:] + l[:n]

def mi(num): #finding the mulitiplicative inverse
    mi = 0
    x = 1
    while mi != 1:
        mi = num * x % 26
        x+=1
    return x-1

def findA(fl,posletters,pn):
    for i in range(len(fl)):
        for j in range(len(pn)):
            if int(pn[j]) * (ord(posletteres[i])-97) % 26 == (ord(fl[i])-97):
                print(int(pn[j]), "is a possible A key")
                return int(pn[j])
    return -1

def decrypt(a,b,ct,alpha): #decrypts the ciphertext
    temp = []
    ts = ""
    mi = 0
    x = 1
    while mi != 1:
        mi = (a * x) % 26
        x+=1
    for i in range(len(ct)):
        if ct[i] != "":
            temp.append(alpha[(x-1)*((ord(ct[i])-97)-b)%26])
        else:
            temp.append(" ")
    ts = "".join(temp)
    return ts

main()

#so first i have a list of frequent letters, then it will loop through to the same frequent letters - 1.
#Then it will have another loop inside which will look through the english letter and then loop again through the english letters - .
#i also have a list of all the frequency of letters for each letter in the alphabet.
#in the frequency section, it will reverse the list so that it can get every single possible combination and print them all out.
#The downside of this is that you have to go through each one to see which makes sense
#i could implement a dictionary that will search through all the combinations and determine which is an english word that makes sense.
#the rest like multiplicative inverse and decrypt are essentially the same as last lab which will find the inverse and determine if it is within the ones we were given
#then the decrypt function will decrypt the message and print it out.

        
        
        
