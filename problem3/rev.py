def rev(s): 
    str = "" 
    for i in s: 
        str = i + str
    return str
x = input("Enter string or number to be reversed:")
print ("The original string is : " + x )
print ("The reversed string is : " + rev(x))
