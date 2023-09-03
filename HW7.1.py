user_input = input()

def rhythm(str):
    str = str.split()
    lst_count = []
    for word in str:
        summ_words = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                summ_words += 1
        lst_count.append(summ_words)
    return len(lst_count) == lst_count.count(lst_count[0])

if rhythm(user_input):
    print(True)
else:
    print(False)
