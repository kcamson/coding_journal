# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# working with lists

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.remove('apple')
fruits.remove('pear')

fruits.append('dragon fruit')
print(fruits)


# working with classes
class MyClass:
    vegetables = ['tomato', 'corn', 'cucumber', 'lettuce']
    vegetables.remove('corn')

    print(vegetables)

    def __init__(self):
        i = 12345

    @staticmethod
    def f():
        return 'whats up??'


print(MyClass.vegetables)
