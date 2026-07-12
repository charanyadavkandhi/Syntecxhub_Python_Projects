def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    if b==0: return "Error: Division by zero"
    return a/b
ops={'+':add,'-':sub,'*':mul,'/':div}
while True:
    print("\n1.Calculate 2.Clear 3.Exit")
    c=input("Choice: ")
    if c=="3": break
    if c=="2":
        print("Cleared"); continue
    try:
        a=float(input("First: ")); op=input("Operator(+,-,*,/): "); b=float(input("Second: "))
        print("Result:", ops[op](a,b))
    except Exception:
        print("Invalid input")
