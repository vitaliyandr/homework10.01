try:  
    n = int(input("Please enter the starting number: "))
    m = int(input("Please enter the final number: "))
    print("Prime numbers between", n, "and", m, "are:")
    for val in range(n, m):
        if val > 1:
            for i in range(2, val):
                if (val % i) == 0:
                    break
            else:
                print(val, end=" ")
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')