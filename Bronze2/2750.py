##버블정렬 이용
def bubbleSort(num,n):
    temp = 0
    for i in range(n): 
        for j in range(n-1-i): 
            if (num[j]>num[j+1]):
                temp = num[j] 
                num[j] = num[j+1]
                num[j+1] = temp
                
if __name__=="__main__":
    num = []
    n = int(input())
    num = [int(input()) for _ in range(n)]
    
    bubbleSort(num,n)
    for i in num:
        print(i)
