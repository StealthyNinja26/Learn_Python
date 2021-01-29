def ispali(a):
    return a[::-1]
x = input ( "Enter string for checking palindrome: ")
y = ispali(x)
if( y == x):
    print("String is a palindrome")
else:
    print("String is not a palindrome")