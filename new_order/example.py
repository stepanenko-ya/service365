n = 2
a = ")("
b = "()"
c = "("
d = ")"
x = set()
for i in range(n):
    x.add(a)
    x.add(b)
    x.add(c)
    x.add(d)
    print("".join(list(x)+list(x)))



