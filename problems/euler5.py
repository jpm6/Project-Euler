'''
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''
top = 20
bucket = 1

for i in range(1,1 + top):
    currentBucket = bucket
    multiple = 1

    while not currentBucket % i == 0:
        currentBucket = bucket * multiple
        multiple += 1
    bucket = currentBucket

print bucket
