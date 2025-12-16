# using recursive
def fib(n):
    if n < 0:
        return "invalid number"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n -1) + fib(n - 2)

num = int(input("Enter the value :"))
res = fib(num)
print(f"The fib {num} is {res}")


# using loop
def fib(n):
    a = 0
    b = 1
    if n <= 0:
        print("There is no fib for nragtive ")
    elif n == 1:
        print(a)
    else:
        print(a, b, end= " ")
        for i in range(2, n):
            c = a + b
            print(c, end = " ")
            a = b
            b = c
num = int(input("Enter the value :"))
res = fib(num)
print(res)