def add(*args):
    a = [n for n in args]
    num = f"{', '.join(map(str, a[0:-1]))} and {a[-1]}"
    print(f"The sum of {num} is {sum(args)}.")

add(1, 2, 3)
