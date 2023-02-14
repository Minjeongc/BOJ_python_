import sys
def recursion(s, l, r):
    global cnt 
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

if __name__ == "__main__":
    num = int(input())

    for _ in range(num):
        cnt = 0
        word = sys.stdin.readline().rstrip('\n')
        i_result = isPalindrome(word)
        print(i_result, cnt)
