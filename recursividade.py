# Esse se trata da sequência de fibbonacci

def fibonacci(i):
    if i<= 0:
        return 0
    elif i==1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)

print(fibonacci(6))