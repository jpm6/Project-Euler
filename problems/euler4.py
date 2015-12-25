'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

x = 999
y = 999
product = x * y
highestPalindrome = 0

def palindrome(n):
    isPalindrome = True
    for i in range(len(str(int(n/2))) - 1):
        if str(n)[i] != str(n)[-i-1]:
            isPalindrome = False
    return isPalindrome

while product > n / 2:
    if x * (y - 1) > (x - 1) * y:
        y = y - 1
    else:
        y = 999
        x = x - 1
    product = x * y
    if palindrome(product) == True and product > highestPalindrome:
        highestPalindrome = product

print highestPalindrome
