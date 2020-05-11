#Return True if it is Prime number
def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(0))# False
print(is_prime(1))# False
print(is_prime(2))# True
print(is_prime(3))# True
print(is_prime(4))# False
print(is_prime(5))#True
print(is_prime(6))#False
print(is_prime(7))# True
print(is_prime(8))# False
print(is_prime(9)) # False
print(is_prime(10))#False
print(is_prime(71))# True
print(is_prime(72))# False
print(is_prime(73))#True