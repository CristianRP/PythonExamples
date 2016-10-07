def draw_square(n):
    print('*'*n)
    for i in range(n - 2):
        print('*' + '*' * (n - 2) + '*')
    print('*'*n)

draw_square(40)