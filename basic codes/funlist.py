#program to print sum of numbers in a list
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print("The sum is:")
print(sum((2, 4, 6, 8, 10,12)))

#program to find max b/w three numbers
def max2( x, y ):
    if x > y:
        return x
    return y
def max3( x, y, z ):
    return max2( x, max2( y, z ) )
print("The max number is:")
print(max3(20, 7, -5))


