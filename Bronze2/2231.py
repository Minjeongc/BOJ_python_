def sort(i):
    j = 0
    j += i
    a = []
    while(i !=0):
        a.append(i%10)
        i = i//10
    for k in a:
        j += k
    return j


if __name__ == "__main__":
    n = int(input())
    result = 1000000
    temp = 0
    for i in range(1,n+1): 
        j = sort(i) ##각자리 수 더한 값 
        if(j == n): ##생성자 조건 만족하면
            print(i)
            break
        if i == n:
            print(0)

            