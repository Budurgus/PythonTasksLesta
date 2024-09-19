Вопрос №1

На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. 

Пример: 

def isEven(value):

      return value % 2 == 0

Решение№1

    isEven = lambda x: x % 2 == 0

Лямбда-функция. 
Плюсы - не обязательно где-то объявлять и явно прописывать, можно налету прописать и вставить код,
если не создаем объект, где указываем напрямую, как однострочную функцию.

Минусы - ограничены одной строкой - не разгуляться.

Плюсы функций - закрытый блок кода, который выполняет определенную логику внутри, можно переиспользовать повторно
в коде. 

Минусы - конкретно выделить минусы в реализации функций не могу, могу только сослаться на плохой код, не состыковку названия с итоговым результатом и прочее, что может сделать
плохой неопытный автор функции.

Вопрос №2

На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

Оценивается:

Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию

Решение №2

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


С использованием списка:

Плюсы: простая реализация и понятный принцип работы

Минусы: неэффективен по памяти

С использованием словарей:

Плюсы: эффективен по памяти за счет использования словарей

Минусы: сложнее реализация и принцип работы

Вопрос №3

На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, почему вы считаете, что функция соответствует заданным критериям.

Решение №3

    def my_sort(nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[-1]
        l_nums = my_sort([n for n in nums[:-1] if n < pivot])
        r_num = my_sort([n for n in nums[:-1] if n > pivot])
        sorted_nums = l_nums + [pivot] + r_num
        return sorted_nums

Вроде как алгоритм быстрой сортировки. Разбивает список чисел на два списка меньших и больших элементов относительно
взятого числа (у нас это последний элемент). После этого рекурсивно повторяем, пока не дойдем до глубины, где у нас
останется 1 или 0 элементов. Должен работать со скоростью O(n*log(n)). Но из минусов - если список отсортирован, то -
наихудший сценарий – O(n²).
