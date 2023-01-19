try:
    for i in range(1,11):
        print("\n\nMULTIPLICATION TABLE FOR %d\n" %(i))
        for j in range(1,11):
            print("%-5d X %5d = %5d" % (i, j, i*j))
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
