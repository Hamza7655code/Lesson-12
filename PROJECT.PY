Lower = int(input("Enter in a upper range: "))
upper = int(input("Enter in a lower range: "))

print("Prime numbers between", Lower, "and", upper, "are: ")
for num in range(Lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)