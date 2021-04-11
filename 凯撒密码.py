def encryption(str,n):
    cipher =[]
    for i in range(len(str)):
        if str[i].islower():
            if ord(str[i]) < 123-n:
                c = chr(ord(str[i])+n)
                cipher.append(c)
            else:
                c = chr(ord(str[i])+n-26)
                cipher.append(c)
        elif str[i].isupper():
            if ord(str[i])<91-n:
                c = chr(ord(str[i])+n)
                cipher.append(c)
            else:
                c = chr(ord(str[i])+n-26)
                cipher.append(c)
        else:
            c= str[i]
            cipher.append(c)
    cipherstr = ('').join(cipher)
    return cipherstr

plaintext = input()
ciphertext = encryption(plaintext,3)
print(ciphertext)