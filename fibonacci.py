def fib(num):
    a, b, counter = 0, 1, 0
    while counter != num:
        yield b
        a, b = b, a + b
        counter += 1

if __name__ == "__main__":
    while True:
        good_number = True
        try:
            num = int(input("How many Fibonacci numbers do you wish to print?\n"))
            if num <1: raise Exception()
        except:
            good_number = False
            print("Please enter an integer that is greater than 0")
        if good_number: break

    print(f"Printing {num} Fibonacci numbers:")
    for i in fib(num):
        print(i)