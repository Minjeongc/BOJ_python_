import sys
dwarf = []
result = 0

for _ in range(9):
    dwarf.append(int(sys.stdin.readline().rstrip('\n')))

dwarf.sort()
sum_dwarf = sum(dwarf) - 100

for i in range(9):
    for j in range(i+1, 9):
        if (dwarf[i] + dwarf[j] == sum_dwarf):
            dwarf.remove(dwarf[i])
            dwarf.remove(dwarf[j-1])
            for k in dwarf:
                print(k)
            exit()

# import itertools

# dwarf = [int(input()) for _ in range(9)]

# for i in itertools.combinations(dwarf, 7):  # 해당 배열을 7명 중복없이 뽑아준다.
#     if sum(i) == 100:  # 그합이 100이라면
#         for j in sorted(i):  # 그 7명을 오름차순으로 정렬후 출력한다.
#             print(j)
#         break #그 후 반복문 탈출