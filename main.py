def add(*args):
    total = 0
    for num in args:
        total+= num
    return total    
# num1 = int(input("Enter 1st num:"))
# num2 = int(input("Enter 2st num:"))
# answer = add(num1,num2)
num =input("Enter numbers: ").split(",")
num = [int(n) for n in num]
print(add(*num))
