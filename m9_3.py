first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
#------------------------------------------
first_result = (len(x) - len(y) for x, y in (zip(first, second)) if len(x) != len(y))
print(list(first_result))
#------------------------------------------
second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))
print(list(second_result))