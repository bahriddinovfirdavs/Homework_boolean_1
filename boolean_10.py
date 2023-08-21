def main(a, b):
    return (a % 2 == 1 or b % 2 == 1) and (a + b) % 2 != 0


print(main(int(input()), int(input())))
