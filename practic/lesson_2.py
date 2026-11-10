import math
import mpmath

def f_bad(x):
    return math.sqrt(x + 1) - math.sqrt(x)

def f_good(x):
    return 1.0 / (math.sqrt(x + 1) + math.sqrt(x))

def f_exact(x):
    mpmath.mp.dps = 50
    mx = mpmath.mpf(x)
    return float(mpmath.sqrt(mx + 1) - mpmath.sqrt(mx))

xs = [10.0**k for k in range(0, 17, 2)]

print(f"{'x':>10} | {'bad':>18} | {'good':>18} | {'error bad':>16} | {'error good':>16}")
print("-" * 90)

for x in xs:
    b = f_bad(x)
    g = f_good(x)
    ex = f_exact(x)
    
    err_b = abs(b - ex) / abs(ex) if ex != 0 else float('inf')
    err_g = abs(g - ex) / abs(ex) if ex != 0 else float('inf')
    
    print(f"{x:>10.0e} | {b:>18.8e} | {g:>18.8e} | {err_b:>16.2e} | {err_g:>16.2e}")