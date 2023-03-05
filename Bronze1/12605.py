testCase= int(input())

for i in range(testCase):
    result = list(map(str, input().split()))
    print("Case #%d: " %(i+1) , end = "")
    for j in range(len(result)-1, -1, -1):
        print(result[j], end = " ")
