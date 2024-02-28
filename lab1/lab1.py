import time
import matplotlib.pyplot as plt
from decimal import Decimal, Context, ROUND_HALF_EVEN

# Recursion


def fibonacci_recursive(i):
    if i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return fibonacci_recursive(i - 1) + fibonacci_recursive(i - 2)

# Dynamic


def fibonacci_dynamic(i):
    fib = [0, 1]
    for i in range(2, i + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[i]

# Arrays


def fibonacci_array(i):
    if i <= 0:
        return "Incorrect Output"
    fib = [0, 1]
    if i > 2:
        for i in range(2, i):
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[i - 1]

# Iterative


def fibonacci_iterative(i):
    a, b = 0, 1
    for _ in range(i):
        a, b = b, a + b
    return a


def fibonacci_matrix(i):
    f = [[1, 1],
         [1, 0]]
    if i == 0:
        return 0
    power(f, i - 1)
    return f[0][0]


def multiply(f, m):
    x = (f[0][0] * m[0][0] + f[0][1] * m[1][0])
    y = (f[0][0] * m[0][1] + f[0][1] * m[1][1])
    z = (f[1][0] * m[0][0] + f[1][1] * m[1][0])
    w = (f[1][0] * m[0][1] + f[1][1] * m[1][1])
    f[0][0] = x
    f[0][1] = y
    f[1][0] = z
    f[1][1] = w


def power(f, i):
    m = [[1, 1], [1, 0]]
    for i in range(2, i + 1):
        multiply(f, m)

# Binet formula


def fibonacci_binet(i):
    ctx = Context(prec=60, rounding=ROUND_HALF_EVEN)
    phi = Decimal((1 + Decimal(5**(1/2))))
    phi2 = Decimal((1 - Decimal(5**(1/2))))

    return int((ctx.power(phi, Decimal(i)) - ctx.power(phi2, Decimal(i))) / (2 ** i * Decimal(5 ** (1 / 2))))

# Function to measure execution time


def measure_time(func, arg):
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    return result, end_time - start_time

# Function to print results in a table


def print_results_table(method_names, input_series, times):
    print(f"{'n':<10} {'Time (seconds)':<20}")
    print("-" * 30)
    for i, time1 in zip(input_series, times):
        print(f"{i:<10} {time1:<20.4f}")
    print("\n")


input_series_1 = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
input_series_2 = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

results = {method.__name__: {'values': [], 'times': []} for method in
           [fibonacci_recursive, fibonacci_dynamic, fibonacci_array, fibonacci_matrix, fibonacci_binet,
            fibonacci_iterative]}

for n in input_series_1:
    _, time_taken = measure_time(fibonacci_recursive, n)
    results['fibonacci_recursive']['times'].append(time_taken)

for n in input_series_2:
    for method in [fibonacci_dynamic, fibonacci_array, fibonacci_matrix, fibonacci_binet, fibonacci_iterative]:
        _, time_taken = measure_time(method, n)
        results[method.__name__]['times'].append(time_taken)

for method_name, data in results.items():
    print(f"Results for {method_name} method:")
    print_results_table(method_name, input_series_1 if method_name == 'fibonacci_recursive' else input_series_2,
                        data['times'])

for method_name, data in results.items():
    plt.figure(figsize=(10, 6))
    if method_name == 'fibonacci_recursive':
        plt.plot(input_series_1, data['times'], marker='o', label=method_name)
        for n, time_taken in zip(input_series_1, data['times']):
            plt.text(n, time_taken, f'{time_taken:.4f} sec', ha='right', va='bottom', fontsize=8)
    else:
        plt.plot(input_series_2, data['times'], marker='o', label=method_name)
        for n, time_taken in zip(input_series_2, data['times']):
            plt.text(n, time_taken, f'{time_taken:.4f} sec', ha='right', va='bottom', fontsize=8)

    plt.title(f'Execution Time for {method_name} method')
    plt.xlabel('n-th Fibonacci Term')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    max_time = max(data['times'])
    if max_time < 1:
        plt.ylim(0, 1)
    else:
        plt.ylim(0, max_time * 1.2)

    plt.show()
