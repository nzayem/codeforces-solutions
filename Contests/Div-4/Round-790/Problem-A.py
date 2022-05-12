t = int(input())

for i in range(t):

    number = input()

    digit_list = list(number)

    print('Yes' if (int(digit_list[0]) + int(digit_list[1]) + int(digit_list[2])) ==
                   (int(digit_list[-1]) + int(digit_list[-2]) + int(digit_list[-3])) else 'No')