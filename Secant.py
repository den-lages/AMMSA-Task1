import math

def secant(f, f1, a, b, e):
    '''
        f - our function, f(x) = 0.
        f1 - determinant of f(x).
        a, b - numbers, limit of our function.
        e - epsilon, limit for iterations.
    '''
    if (f(a)*f1(a) >= 0):
        c = a
    else:
        c = b
    
    while(True):
        if (f(a)*f1(a) < 0):
            x = a
            x1 = f(x) * (x - c) / (f(x) - f(c))
            x = x - x1
        else:
            x = b
            x1 = f(x) * (x - c) / (f(x) - f(c))
            x = x - x1
        
        if (math.fabs(x1) > e):
            return x

f = lambda x: ((x-5)**2 - math.sin(x-5))
f1 = lambda x: (math.sin(x-5) + 2)

a = 4.85
b = 5.2
e = 0.00001

solution = secant(f, f1, a, b, e)
print(solution)

        