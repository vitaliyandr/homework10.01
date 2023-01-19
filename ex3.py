try:
    a = int(input("a-> "))
    b = int(input("b-> "))
    for i in range(1, 11):
        print(str(a), "*", str(i), "=", a * i, end="" + " ")
    print()
    print("-" * 112)
    for i in range(1, 11):
        print(str(b), "*", str(i), "=", b * i, end="" + " ")
    print()
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')