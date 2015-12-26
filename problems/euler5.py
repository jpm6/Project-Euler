'''
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

result = 0
start = 1
end = 1000
my_list = []

def divisible(n):
    divisible = True
    for i in range(11,21):
        if n % i != 0:
            divisible = False

    return divisible

while len(my_list) == 0:
    my_list = [x for x in range(start,end) if divisible(x)]
    start = end
    end = end * 2
print my_list
