# find a prime number: prime number fuction
def prime_number(n):
    n = int(input("Enter a number: "))
    if n < 1:
        print("Enter a number greater than one!")
    else:
        for i in range(2, n):
            if n % 2 == 0:
                print("Not a prime number")
                break
        else:
            print("'Is a prime number'")

prime = prime_number(8)
prime_number(prime)