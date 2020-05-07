#Is_A_Number_Prime
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def main():
    value = int(input("Enter a number: "))
    if isprime(value):
        print(value, "is a prime number")
    else:
        print(value, "is not a prime number")
if __name__ == "__main__":
    main()
