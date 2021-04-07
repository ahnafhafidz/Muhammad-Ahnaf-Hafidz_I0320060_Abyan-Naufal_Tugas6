for bilangan in range(10,25):
    for i in range(2, bilangan):
        if (bilangan % i) == 0:
            print(bilangan,"bukan bilangan prima")
            break
    else:
        print(bilangan,"adalah bilangan prima")
