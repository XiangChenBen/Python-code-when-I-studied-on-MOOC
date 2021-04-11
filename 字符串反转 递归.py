def rev(s):
    if s == "" :
        return s
    else : 
        return rev(s[1:])+s[0]
Str = input("please input s string:")
print(rev(Str))