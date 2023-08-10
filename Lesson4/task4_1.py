#4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Если таких чисел нет - выдать внятное диагностическое сообщение


num_list_1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
num_list_2 = [3, 6, 9, 12, 15, 18]
#num_list_1 = [2, 4, 6, 8, 10, 10, 8, 6, 4, 2]
#num_list_2 = [3, 9, 12, 15, 18]

res = []
num_list3 =list(set(num_list_1)) +list(set(num_list_2))
print(num_list3)
checked_nums_list = []
for i in num_list3:
    if num_list3.count(i) > 1 and i not in checked_nums_list:
        checked_nums_list.append(i)
        res.append(i)
if not res:
    print('Повторяющихся чисел нет')
else:
    print(*res)  
