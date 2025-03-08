import numpy as np

def euler_method(f, t0, y0, h, n):
    t = t0
    y = y0
    for _ in range(n):
        y += h * f(t, y)
        t += h
    return y

def runge_kutta_method(f, t0, y0, h, n):
    t = t0
    y = y0
    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
    return y

def function(t, y):
    return t - y**2

if __name__ == "__main__":
    t0, y0 = 0, 1  # Initial conditions
    t_end, steps = 2, 10  # Range and iterations
    h = (t_end - t0) / steps  # Step size
    
    euler_result = euler_method(function, t0, y0, h, steps)
    runge_kutta_result = runge_kutta_method(function, t0, y0, h, steps)
    
    print(euler_result)  # Expected: 1.2446380979332121
    print(runge_kutta_result)  # Expected: 1.251316587879806
