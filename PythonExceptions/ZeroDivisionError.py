

a = eval(input("Enter a:"))
b = eval(input("Enter b:"))
c = a / b;
print("a/b = %d" % c)





try:
    a = eval(input("Enter a:"))
    b = eval(input("Enter b:"))
    c = a / b;
    print("a/b = %d" % c)
except Exception:
    print("can't divide by zero")
else:
    print("Hi I am else block")
