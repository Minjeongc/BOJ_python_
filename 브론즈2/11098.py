test_case = int(input())

for _ in range(test_case):
    p_num = int(input())
    p_salary = []
    p_name = []

    for i in range(p_num):
        salary , name = map(str, input().split())
        p_salary.append(int(salary))
        p_name.append(name)

    #max_salary = max(p_salary)
    p_index = p_salary.index(max(p_salary))
    print(p_name[p_index])



