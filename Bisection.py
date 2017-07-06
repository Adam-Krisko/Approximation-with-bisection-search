

## This is an example of a bisection search 

x = int(input('Enter a number: '))
epsilon = 0.01
numGuesses = 0
low = 0.0 ## we take a lower and an upper bound on the search space
high = max(x, 1.0)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    print('low: ',low, ' high: ', high,' ans: ', ans)
    numGuesses += 1 ## += means incrementing the value of the answer by what is on the right side
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('Number of guesses = ', numGuesses)
print(ans, 'is close to square root of', x)


## This is an example of a bisection search 


