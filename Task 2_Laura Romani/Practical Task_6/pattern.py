rows = 5
star = "*"

for i in range(1, rows * 2):
    if i <= rows:
        print(star * i)
    else:
        print(star * (rows * 2 - i))

# this small program was very difficult to compile, it is not straightforward at all.