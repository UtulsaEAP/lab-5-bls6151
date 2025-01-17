#Name: Braden Stanfield   Lab: Fri 3
def fibonacci(n):
    #write your code here
    num1 = 0
    num2 = 1
    num3 = 0
    i = 1
    if n == 0:
        num3 = 0
    elif n > -1:
        while i < n:
            num3 = num1 + num2
            num1 = num2
            num2 = num3
            i += 1
    else:
        num3 = -1
    return num3


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')