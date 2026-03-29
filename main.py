def add(*args):
    total = 0
    for num in args:
        total+= num
    return total    
# num1 = int(input("Enter 1st num:"))
# num2 = int(input("Enter 2st num:"))
# answer = add(num1,num2)
lalaa =input("Enter numbers: ").split(",")
n=[]
for i in lalaa:
    n.append(int(i))
print(add(*n))