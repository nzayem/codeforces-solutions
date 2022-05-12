t = int(input())  # test cases

for i in range(t):

    numbers = input()
    x = int(numbers.split(' ')[0])
    y = int(numbers.split(' ')[1])

    if x == y:
        print(3, 1)
    
    elif x >= y or y % x != 0:
        print(0, 0)

    else:
        print(1, int(y / x))