num_test = int(input())

for i in range(num_test):
    r, s = input().split()
    r = int(r)
    string = ''

    for j in s:
        for k in range(r):
            string = string + j

    print(string)
    