# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = 'Российская российская компания в сфере онлайн-образования, основанная в 2010 году. ' \
       'Образовательная платформа GeekBrains предлагает курсы по информационным технологиям, программированию, ' \
       'аналитике, тестированию, маркетингу, управлению и дизайну. С 2016 года входит в состав VK.'


my_dict = {}
COUNT = 10
NOT_NEED = ',.!?-'

for i in NOT_NEED:
    text = ' '.join(text.split(i))
my_list = text.lower().split()

for word in my_list:
    if word not in my_dict.keys():
        my_dict[word] = my_list.count(word)

for i in range(COUNT):
    result = list(my_dict.keys())[list(my_dict.values()).index(max(my_dict.values()))]
    print(result)
    my_dict.pop(result)
