num_test = int(input())

test_taker = list(map(int, input().split()))

viewer = list(map(int, input().split()))

minimum = num_test


for i in test_taker:
    i -= viewer[0]

    if i>0:
        if i%viewer[1]:
            minimum += (i//viewer[1])+1
        else:
            minimum += (i//viewer[1])


print(minimum)