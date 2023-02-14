import sys

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        arr = list(map(str, sys.stdin.readline().rstrip('\n').split()))
        result = 0
        for i in range(len(arr)):
            if arr[i] == '@':
                result *= 3
            elif arr[i] == '%':
                result += 5 
            elif arr[i] == '#':
                result -= 7
            else:
                result += float(arr[i])
        
        print(f"{result:.2f}")
            

