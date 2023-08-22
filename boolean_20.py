def main(a):
    b = a % 10
    c = (a // 10) % 10
    d = (a // 100) % 10
    e = a // 1000
    return b != c and b != d and b != e and c != d and c != e and d != e


print(main(int(input())))
