word = input().upper()

word_del = list(set(word))

cnt_list = []
cnt = 0
max_cnt = 0
max_word = ''

for i in word_del:
    cnt = word.count(i)
    cnt_list.append(cnt)
    if cnt > max_cnt:
        max_cnt = cnt
        max_word = i

    
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(max_word)
