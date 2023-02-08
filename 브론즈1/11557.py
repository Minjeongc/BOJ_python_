
test_case = int(input())

for _ in range(test_case):
    school_list = []
    num = int(input())
    for i in range(num):
        school, alcohol = input().split()
        school_list.append([school, int(alcohol)])

    school_list.sort(key = lambda x : (x[1],x[0]))
    print(school_list[-1][0])