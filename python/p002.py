def p002(x):
    def fibonacci(a0, a1):
        return a0 + a1
    
    a0 = 1
    a1 = 2
    r = 2
    
    a2 = fibonacci(a0, a1)
    while a2 < x:
         r += a2 if (a2 % 2 == 0) else 0
         a0 = a1
         a1 = a2
         a2 = fibonacci(a0, a1)
    
    return r
