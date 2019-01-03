def generate_primes(n):
    # Assume all integers from 2 ... n are prime
    primes = [True for _ in range(n + 1)]
    primes[0] = False
    primes[1] = False

    for i in range(2, n + 1):
        if primes[i]:
            for j in range(2, n + 1):
                if i * j > len(primes) - 1:
                    break
                primes[i * j] = False

    output = []
    for i in range(len(primes)):
        if primes[i]:
            output.append(i)
    return output

print(generate_primes(100))
