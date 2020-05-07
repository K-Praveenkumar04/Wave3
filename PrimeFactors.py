#PrimeFactors
number = int(input("Enter a number that is equal or greater than 2: "))
n = 2
print ("The prime factors of " + str(number) + " are: ")
while n * n <= number:
    if number % n:
        n += 1
    else:
        number //= n  
    print(n)
