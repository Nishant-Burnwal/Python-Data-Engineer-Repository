def isPrime(n):
    """
        Checks for the primes numbers
    """
    sqrt_n = int(n ** 0.5)
    if n < 2:
        return False
    else:
        for i in range(2, sqrt_n + 1):
            if n % i == 0:
                return False
        return True
    
# taking user input for range to check primes
n1 = int(input("Enter the Range 1 number: "))
n2 = int(input("Enter the Range 2 number: "))
# creating a empty primes list
primes = []

for i in range(n1, n2 + 1):
    if isPrime(i):
        primes.append(i)

if (len(primes) == 0):
    print("No Prime number found.")
else:
    print(primes)

    
        
