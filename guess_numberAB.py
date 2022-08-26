import random

answer = random.sample(range(1, 10), 4)
print(answer)

while True:
    quess = input('請猜一個不包含零且不重複的四位數,例如1234:')
    a = b = 0
    qes = [int(n) for n in list(quess)]
    # check 
    for i in range(4):
        if qes[i] in answer:
            if qes[i] == answer[i]:
                a += 1
            else:
                b += 1
    if a == 4:
        print('恭喜答對！正確答案為：', answer)
        break
    
    print(f'猜測結果為：{a}A{b}B, 請再接再厲！')



        



