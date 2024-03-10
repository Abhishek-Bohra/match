a = int(input("Enter the number from 1-10: "))
match a:
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
        for i in range(1, 11):
            print(f"{a} x {i} = {a * i}")
    case _:
        print("Not in range of 1 to 10")