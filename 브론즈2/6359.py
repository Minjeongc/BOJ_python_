test = int(input())
for i in range(test):

    N= int (input())

    arr = [ 0 ] * N
    result= 0
    # 0: 닫, 1: 열
    for i in range(1,N+1):
        for j in range(i-1,N):
            if ((j+1) % i) ==0:
                if arr[j] == 0:
                    arr [j] = 1
                else:
                    arr [j] = 0


    for i in arr:
        if i == 1:
            result +=1 
    print(result)