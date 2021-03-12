import math

def bisection(f, a, b, e):
    '''
        f - our function, f(x) = 0.
        a, b - numbers, limit of our function.
        e - epsilon, limit for iterations.
    '''
    if f(a)*f(b) >= 0:
        print("Bisection method fails...")
        return None
    
    while (math.fabs(b-a) > 2*e):
       x = (a + b)/2

       if (f(a)*f(x)) < 0:
           b = x
       elif (f(b)*f(x)) < 0:
           a = x
       elif f(x) == 0:
            print("Exact solution was found.")
            return x
       else:
            print("Bisection method failed.")
            return None
    
    return (a + b)/2
    

f = lambda x: (x-5)**2-math.sin(x-5)
a = 4.85
b = 5.2
e = 0.000001

solution = bisection(f, a, b, e)
print(solution)

