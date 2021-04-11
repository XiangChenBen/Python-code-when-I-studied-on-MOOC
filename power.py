class powerpo()
def Po(a ,b, c =1):
    if b == 0 :
        return c
    else :
        c = Po(a,b-1)*a
    return c

x = eval(input("base"))
y = eval(input("power"))
print("{}".format(Po(x,y)))