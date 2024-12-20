import time
import tracemalloc
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, mood, hunger, tiredness):
        self._name = name
        self._mood = mood
        self._hunger = hunger
        self._tiredness = tiredness

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, value):
        self._mood = value

    @property
    def hunger(self):
        return self._hunger

    @hunger.setter
    def hunger(self, value):
        if 0 <= value <= 10:
            self._hunger = value
        else:
            raise ValueError("Hunger value must be between 0 and 10")

    @property
    def tiredness(self):
        return self._tiredness

    @tiredness.setter
    def tiredness(self, value):
        self._tiredness = value

    @abstractmethod
    def speak(self):
        pass

    def feed(self):
        self.hunger -= 3
        self.mood = "happy"
        print(f"{self._name} is fed. Hunger: {self.hunger}, Mood: {self.mood}")

    def rest(self):
        self.tiredness -= 3
        self.mood = "relaxed"
        print(f"{self._name} is rested. Tiredness: {self.tiredness}, Mood: {self.mood}")

    def play(self, toy):
        if toy.is_fun:
            self.mood = "happy"
            self.tiredness += 2
            print(f"{self._name} is playing with {toy.name}. Mood: {self.mood}, Tiredness: {self.tiredness}")
        else:
            self.mood = "bored"
            print(f"{self._name} is bored with {toy.name}. Mood: {self.mood}")

class Dog(Animal):
    def __init__(self, name, mood, hunger=5, tiredness=5):
        super().__init__(name, mood, hunger, tiredness)

    def speak(self):
        if self.hunger > 7:
            return "Woof! I'm hungry!"
        elif self.tiredness > 7:
            return "Woof! I'm tired!"
        elif self.mood == "happy":
            return "Woof! I'm happy!"
        else:
            return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        if self.hunger > 7:
            return "Meow! I'm hungry!"
        elif self.tiredness > 7:
            return "Meow! I'm tired!"
        else:
            return "Meow! Meow!"

class Parrot(Animal):
    def speak(self):
        if self.hunger > 7:
            return "Squawk! I'm hungry!"
        elif self.tiredness > 7:
            return "Squawk! I'm tired!"
        else:
            return "Squawk! Squawk!"

class Toy:
    def __init__(self, name, is_fun):
        self.name = name
        self.is_fun = is_fun

class MyContainer:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"MyContainer with {len(self.items)} items"

    def __getitem__(self, index):
        return self.items[index]

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

def modify_list(l):
    for i in range(len(l)):
        if isinstance(l[i], list):
            modify_list(l[i])
        else:
            l[i] = "modified"

def modify_tuple(t):
    for i in range(len(t)):
        if isinstance(t[i], tuple):
            modify_tuple(t[i])
        else:
            t[i] = "modified"

def list_tuple_operations_deep(lst, tpl):
    start_list = time.time()
    modify_list(lst)
    end_list = time.time()
    list_time = end_list - start_list

    start_tuple = time.time()
    try:
        modify_tuple(tpl)
    except TypeError as e:
        error_message = str(e)
    end_tuple = time.time()
    tuple_time = end_tuple - start_tuple

    return lst, error_message, list_time, tuple_time

def square_numbers(n):
    return [i**2 for i in range(1, n+1)]

def square_numbers_generator(n):
    return (i**2 for i in range(1, n+1))

def memory_usage_comparison(n):
    tracemalloc.start()

    list_result = square_numbers(n)
    list_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()
    tracemalloc.start()

    generator_result = list(square_numbers_generator(n))
    generator_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return list_memory, generator_memory

