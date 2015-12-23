'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

limit = 600851475143

possiblePrimes = range(2, int(limit ** .5))

for i in possiblePrimes:
    possiblePrimes = filter(lambda x: (x % i != 0 or x <= i) and limit % x == 0, possiblePrimes)

print possiblePrimes[-1]
