from abc import ABC, abstractmethod


class CycleFifo(ABC):
    def __init__(self, max_size=1):
        self.max_size = max_size
        self.size = 0

    @abstractmethod
    def __str__(self):
        pass

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0

    @abstractmethod
    def append(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass


class CycleFifoList(CycleFifo):
    def __init__(self, max_size=1):
        super().__init__(max_size)
        self.buffer = []

    def __str__(self):
        return f"{self.buffer}"

    def append(self, item):
        if self.is_full():
            print("Buffer is full")
            return None
        self.buffer.append(item)
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Buffer is empty")
            return None
        self.size -= 1
        return self.buffer.pop(0)


class CycleFifoDict(CycleFifo):
    def __init__(self, max_size=1):
        super().__init__(max_size)
        self.buffer = {}
        self.head = 0
        self.tail = 0

    def __str__(self):
        return f"{list(self.buffer)}"

    def append(self, item):
        if self.is_full():
            print("Buffer is full")
            return None
        self.buffer.setdefault(self.head, item)
        self.size += 1
        self.head = (self.head + 1) % self.max_size

    def pop(self):
        if self.is_empty():
            print("Buffer is empty")
            return None
        elem = self.buffer.pop(self.tail)
        self.size -= 1
        self.tail = (self.tail + 1) % self.max_size
        return elem

'''
С использованием списка:
Плюсы: простая реализация и понятный принцип работы

Минусы: неэффективен по памяти

С использованием словарей:
Плюсы: эффективен по памяти за счет использования словарей

Минусы: сложнее реализация и принцип работы
'''