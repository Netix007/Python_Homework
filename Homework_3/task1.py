my_dict = {'Alex': ('спички', 'продукты', 'топор', 'гитара'),
           'Sergey': ('спички', 'продукты', 'палатка', 'фонарик'),
           'Vasiliy': ('спички', 'продукты', 'фонарик', 'котелок'),
           }

names = list(my_dict.keys())
answer1 = set(my_dict.get(names[0]))
for value in my_dict.values():
    answer1 = answer1.intersection(value)
if len(answer1) != 0:
    print(f'Все друзья взяли с собой {answer1}')
else:
    print('Общих вещей нет')

answer2 = set()
for name in my_dict.keys():
    unique_things = set(my_dict.get(name))
    for key, value in my_dict.items():
        if name != key:
            unique_things -= set(value)
    answer2 = answer2.union(unique_things)
if len(answer2) != 0:
    print(f'Уникальные вещи: {answer2}: ')

for name in my_dict.keys():
    flag = True
    for key, value in my_dict.items():
        if name != key:
            if flag:
                answer3 = set(value)
                flag = False
            answer3 = answer3.intersection(value)
    answer3 -= answer1
    if len(answer3) != 0:
        print(f'Следующие вещи: {answer3}, есть у всех кроме {name}')
