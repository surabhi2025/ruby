from abc import ABC, abstractmethod

class ABsclass(ABC):


    def print(self, x):
        print("Passed value", x)


    @abstractmethod
    def task(self):
        print("We are inside Abclass task")


class test_class(ABsclass):
    def task(self):
        print("WE are inside test_class trask")


test_obj = test_class()
test_obj.task()
test_obj.print(100)