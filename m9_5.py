class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step != 0:
            self.step = step
        else:
            raise StepValueError

    def __iter__(self):
        self.pointer = self.start
        self.pointer -= self.step
        return self

    def __next__(self):
        if self.step > 0 and self.pointer < self.stop or self.step < 0 and self.pointer > self.stop:
            self.pointer += self.step
            return self.pointer
        # elif self.step < 0 and self.pointer > self.stop:
        #     self.pointer += self.step
        #     return self.pointer
        raise StopIteration('stop')
print('iter1:')
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

# =====   test   =====   =====   =====   =====

iter2 = Iterator(-5, 1)
# print(list(iter2))
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

print('iter2:')
for i in iter2:
    print(i, end=' ')
print()
print('iter3:')
for i in iter3:
    print(i, end=' ')
print()
print('iter4:')
for i in iter4:
    print(i, end=' ')
print()
print('iter5:')
for i in iter5:
    print(i, end=' ')
print()
