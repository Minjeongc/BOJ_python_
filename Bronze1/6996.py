test_case = int(input())

for _ in range(test_case):
    word1 , word2 = map(str, input().split())

    word3 = sorted(list(word1))
    word4 = sorted(list(word2))
    
    if word3 == word4:
        print("%s & %s are anagrams." %(word1, word2))
    else:
        print("%s & %s are NOT anagrams." %(word1, word2))
