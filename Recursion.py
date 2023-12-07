def f(n):
    if n>1:
        return n+(f(n-1))
    else:
        return n
p=int(input("enter p: "))
print(f(p))



"""#lambda fuction
root_1=lambda a,b,c: (-b +((b**2-4*a*c)**0.5))/(2**a)
root_2=lambda a,b,c: (-b -((b**2-4*a*c)**0.5))/(2**a)
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
ptint(root_1(a,b,c))
print(root_2(a,b,c))
"""
