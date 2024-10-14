def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def multi(p,q):
    return p*q
def div(p,q):
    return p/q
print("Enter your choise:")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")
choise=input("Enter a letter(a/b/c/d/):")
p1=int(input("Enter the first number:"))
q1=int(input("Enter the second number:"))
if (choise=="a"):
    print(p1,"+", q1 ,"=", add(p1,q1))
elif(choise=="b"):
    print( p1 ,"-" ,q1, "=", sub(p1,q1))
elif(choise=="c"):
    print(p1 ,"*",q1,"=", multi(p1,q1))
elif(choise=="d"):
    print(p1,"/",q1,"=", div(p1,q1))
else:
    print("Error!")