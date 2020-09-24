n = abs(int(input("Enter a number ")))

base = ["(", ")"]
                    # это для 1
if n == 1:
    one = "".join(base)
    print(one)

elif n != 0:
                    # это для 2 и более
    one = "".join(base)
    print(one * n)
    first = " ".join(base[0])
    last = " ".join(base[1])
    base_base = "".join(base) * (n-1)
    x = first + base_base + last
    print(x)
    if base_base > "()":
        print(first * (n-1) + ''.join(base) + last * (n-1))


