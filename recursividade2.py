# f(n) = a^n

def f(a, n):  # Não vai segurar números estratosféricos
    if n == 0:
        return 1
    elif n < 0:
        return 1/ f(a, -n)
    else:
        return a * f(a, n-1)
print(f(3, 4))

# OU 

# print(8 ** 2) 
# print(2 ** 4)

