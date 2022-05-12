t = int(input())

for i in range(t):

    total_boxes = int(input())

    content = input().split(' ')

    content_int = []

    for number in content:
        content_int.append(int(number))

    results = [x - min(content_int) for x in content_int]

    final = 0

    for result in results:

        final += result

    print(final)
