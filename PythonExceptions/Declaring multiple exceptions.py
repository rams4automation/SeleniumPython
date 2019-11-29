try:
    a=10/0;
except ArithmeticError:
    print("Arithmetic Exception")
else:
    print ("Successfully Done")