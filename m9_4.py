# ===== lambda =====
first = 'Мама мыла раму'
second = 'Рамена мало было'
# ----- test -------
print(list(map(lambda x, y: x == y, first, second)))

# ===== замыкание =====
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            file.write('')
        for line in data_set:
            print(line)
            with open(file_name, 'a', encoding='utf8') as file:
                file.write(str(line))
                file.write('\n')
    return write_everything
# ----- test -------
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# ===== __call__ =====
import random
class MysticBall:
    def __init__(self, *args):
        self.words = [x for x in args]
    def __call__(self):
        return random.choice(self.words)
first_ball = MysticBall('Да', 'Нет', 'Наверное')
# ----- test -------
print(first_ball())
print(first_ball())
print(first_ball())