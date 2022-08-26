# loop star
a = 15
for i in range(1,a):
    print('*'*i)

# star pyramid
a = 15
for i in range(1, a):
    d = 2
    x = '*' * (1+i*d-2)
    print(f'{x:^27s}')