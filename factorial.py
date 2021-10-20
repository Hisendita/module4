"""
def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
"""

def factorial_recursive(num):
    if num == 1:
        return 1
    return num*factorial_recursive(num-1)

print(factorial_recursive(5))